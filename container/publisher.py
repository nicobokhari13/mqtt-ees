from typing import Dict
from copy import deepcopy
from container.topic import Topic_Container
import random
from config.config_utils import ConfigUtils

topic_c = Topic_Container()
config_file = ConfigUtils()

class Network:
    _instance = None
    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance
    
    def __init__(self) -> None:
        self._devices: Dict[str, Device] = dict()
        self._all_devices_energy_consumption = 0

    # Called after completing a round for 1 algorithm
    def resetUnits(self):
        for device in self._devices.values():
            device.resetAssignments()
            device._consumption = 0
            device._battery = 100
            device.setExecutions(new_value=0)
            device._sense_timestamp = []

    def clearUnits(self):
        self._devices.clear()

    def clearAllDeviceEnergyConsumption(self):
        self._all_devices_energy_consumption = 0
        
    def calculateTotalEnergyConsumption(self):
        for device in self._devices.values():
            executions = device.effectiveExecutions()
            device_energy_used = config_file.SENSE_ENERGY * len(device._sense_timestamp) + config_file.COMM_ENERGY * executions
            self._all_devices_energy_consumption += device_energy_used

class Device:

    def __init__(self):
        self._assignments = {} # topic: publishing latency
        self._battery = 100 # p.allEnergyCapacity
        self._consumption = 0 # Ecurrent in the MQTTCC algo
        self._capable_topics = []
        self._num_executions_per_hour = 0
        # For calculating total energy consumption (for all algorithms)
        self._sense_timestamp = []

    def setMac(self, mac):
        self._device_mac = mac

    def addTimestamp(self, timestamp):
        self._sense_timestamp.append(timestamp)

    def addAssignment(self, added_topic, added_qos):
        self._assignments[added_topic] = added_qos
    
    def resetAssignments(self):
        self._assignments.clear()    

    def setCapableTopics(self, capability:list):
        self._capable_topics = capability    

    def capableOfPublishing(self, topic):
        if topic in self._capable_topics:
            return True
        else:
            return False
        
    def setExecutions(self, new_value):
        self._num_executions_per_hour = new_value

    def updateConsumption(self, energy_increase):
        self._consumption += energy_increase

    def effectiveExecutions(self, new_task_timestamp = None):
        tail_window = config_file.DEFAULT_TAIL_WINDOW_MS
        time_stamps = list(self._sense_timestamp)
        if new_task_timestamp:
            time_stamps.append(new_task_timestamp)
        if not time_stamps:
            return 0
        time_stamps.sort()
        last_execution_end = -tail_window
        effective_executions = 0
        for time in time_stamps:
            if time >= last_execution_end + tail_window:
                effective_executions+=1
                last_execution_end = time
        return effective_executions

    def energyIncrease(self, task_timestamp):
        newExecutions = self.effectiveExecutions(new_task_timestamp=task_timestamp)
        changeInExecutions = newExecutions - self._num_executions_per_hour
        # the change in the number of sensing events = 1
        # change in the number of communication events is the change in effective executions
        energyUsed = config_file.SENSE_ENERGY + changeInExecutions * config_file.COMM_ENERGY
        return energyUsed

class Publisher_Container:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance
    
    def __init__(self) -> None:
        self._publishers = Network()
        self._total_devices = 0

    def setTotalDevices(self, num_devs):
        self._total_devices = num_devs

    # Precondition: numPubs is a whole number > 0
    def generatePublisherMacs(self):
        pub_macs = []
        for i in range(self._total_devices):
            name = f"dev-{i}"
            pub_macs.append(name)
        return pub_macs

    def setupDevices(self):
        print(f"creating {self._total_devices} devices")
        device_macs = self.generatePublisherMacs()
        for mac in device_macs:
            self._publishers._devices[mac] = Device()
            self._publishers._devices[mac].setMac(mac)
        self.generateDeviceCapability()
    
    # Precondition: Topics are created 
    def generateDeviceCapability(self):
        found = False
        for unit in self._publishers._devices.values():
            num_capable_publishes = random.randint(a=2, b=topic_c._total_topics)
            # randomly sample this number of topics with their max_allowed_latency
            publishes = random.sample(population=sorted(topic_c._topic_dict.keys()), k=num_capable_publishes)
            unit.setCapableTopics(capability=publishes)
        for topic in topic_c._topic_dict.keys():
            for unit in self._publishers._devices.values():
                if unit.capableOfPublishing(topic):
                    found = True
                    break
            if not found:
                # if the topic is not covered by any device
                # get a random device
                rand_mac = random.choice(list(self._publishers._devices.keys()))
                # assign the topic t topicInCapable(self,)o it
                self._publishers._devices[rand_mac]._capable_topics.append(topic)
            # reset found to False
            found = False
        # all topic capabilities are created, saved, and cover all topics
            

        

            