from container.publisher import Publisher_Container
from container.topic import Topic_Container
from container.subscriber import Subscriber_Container
from copy import deepcopy
from config.config_utils import ConfigUtils

#------------------------------------------#


# to access the singleton instance easily
pub_c = Publisher_Container()
sub_c = Subscriber_Container()
topic_c = Topic_Container()

class MQTTEES:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance
    
    def __init__(self):
        self._algo_name = "cc"
        self._total_energy_consumption = 0
    
    # system capability used to track which publishers can publish to
    def copyOfSystemCapability(self, capability:dict):
        self._system_capability = deepcopy(capability)

    # timeline used to calculate total energy consumption
    def copyOfTopicTimeStamps(self, timestamps):
        self._experiment_timeline = deepcopy(timestamps)
        
    def resetTotalConsumption(self):
        self._total_energy_consumption = 0
    
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
            print("topic list", tmin, self._experiment_timeline[tmin])
            # if the list at this key is empty, remove the key
            del self._experiment_timeline[tmin]
        
        return [tmin, fmin]

    def mqttees_algo(self):
        endAlgo = False
        while len(self._experiment_timeline.keys()) > 0:
            [newTask, newTaskTimeStamp] = self.findNextTask()
            print("topic ", newTask, " time ", newTaskTimeStamp)
            Emin = -1
            Einc = None
            EincMin = None
            Enew = None
            Eratio = None
            bestMac = None
            for deviceMac in self._system_capability[newTask]:
                # for each device capable of publishing to newTask
                # calculate energy increase from adding the new task
                Einc = pub_c._publishers._devices[deviceMac].energyIncrease(newTaskTimeStamp)
                Enew = pub_c._publishers._devices[deviceMac]._consumption + Einc
                Eratio = Enew / pub_c._publishers._devices[deviceMac]._battery
                if (Emin < 0) or (Enew <= pub_c._publishers._devices[deviceMac]._battery and Eratio < Emin):
                    bestMac = deviceMac
                    Emin = Eratio 
                    EincMin = Einc
                if (Enew >= pub_c._publishers._devices[deviceMac]._battery):
                    print("last time = ",newTaskTimeStamp)
                    endAlgo = True
                    # exit algorithm
                if endAlgo:
                    break
            if endAlgo:
                print("leaving mqtt_cc algo")
                return newTaskTimeStamp 
            if bestMac:
                # After each allocation
                    # update the consumption
                    # add the timestmap
                    # update the number of executions since efficient energy index depends on executions
                pub_c._publishers._devices[bestMac].updateConsumption(EincMin)
                pub_c._publishers._devices[bestMac].addTimestamp(timestamp=newTaskTimeStamp)
                bestMac_new_executions = pub_c._publishers._devices[bestMac].effectiveExecutions()
                pub_c._publishers._devices[bestMac].setExecutions(new_value=bestMac_new_executions)
        return None