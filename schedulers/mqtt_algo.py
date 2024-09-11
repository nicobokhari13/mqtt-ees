from container.publisher import Publisher_Container
from container.topic import Topic_Container
from container.subscriber import Subscriber_Container
from copy import deepcopy
import random 
from config.config_utils import ConfigUtils


# to access the singleton instance easily
pub_c = Publisher_Container()
sub_c = Subscriber_Container()
topic_c = Topic_Container()

class Standard:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance
    
    def __init__(self):
        self._total_energy_consumption = 0

    def copyOfSystemCapability(self, capability):
        # a dictionary where 
        #   key = topic
        #   value = [deviceMacs of devices that can publish to the key topic] 
        self._system_capability = deepcopy(capability)

    def copyOfTopicTimeStamps(self, timestamps):
        # a dictionary with each topic's sense execution timestamp < T observation period
            # topic/1: [10,20,30...]
        self._experiment_timeline = deepcopy(timestamps)
        
    def findNextTask(self):
        fmin = -1
        tmin = None
        for topic in topic_c._topic_dict.keys():
            # get the first timestamp for that topic
            if topic in self._experiment_timeline.keys():
                fi = self._experiment_timeline[topic][0] 
            # if its min, set it as min
                if (fmin < 0) or (fi < fmin):
                    tmin = topic
                    fmin = fi
        # at this point fmin holds the next timestamp, and tmin holds which topic to publish to
        # remove the timestamp from the topic's list
        if tmin:
            self._experiment_timeline[tmin].pop(0)

        if not self._experiment_timeline[tmin]:
            print(tmin, self._experiment_timeline[tmin])
            # if the list at this key is empty, remove the key
            del self._experiment_timeline[tmin]
        
        return [tmin, fmin]

    def mqtt_algo(self):
        endAlgo = False
        while len(self._experiment_timeline.keys()) > 0:
            [newTask, newTaskTimeStamp] = self.findNextTask()
            print("time = ", newTaskTimeStamp)
            for deviceMac in self._system_capability[newTask]:
                energyIncrease = pub_c._publishers._devices[deviceMac].energyIncrease(task_timestamp=newTaskTimeStamp)
                if energyIncrease + pub_c._publishers._devices[deviceMac]._consumption >= pub_c._publishers._devices[deviceMac]._battery:
                    endAlgo = True
                else:
                    pub_c._publishers._devices[deviceMac].updateConsumption(energyIncrease)
                    pub_c._publishers._devices[deviceMac].addTimestamp(timestamp=newTaskTimeStamp)
                    pub_c._publishers._devices[deviceMac].setExecutions(new_value=pub_c._publishers._devices[deviceMac].effectiveExecutions())
                if endAlgo:
                    print("leaving standard mqtt algo")
                    break
            if endAlgo:
                print("leaving standard mqtt algo")
                return newTaskTimeStamp
        print("done with standard algo")
        return None
                  
