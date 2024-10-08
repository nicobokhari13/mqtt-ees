from container.publisher import Publisher_Container
from container.topic import Topic_Container
from container.subscriber import Subscriber_Container
from copy import deepcopy
import random 
from config.config_utils import ConfigUtils

#------------------------------------------#

# to access the singleton instance easily
pub_c = Publisher_Container()
sub_c = Subscriber_Container()
topic_c = Topic_Container()

#------------------------------------------#

class Random:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance
    
    def __init__(self):
        self._algo_name = "random"
        self._total_energy_consumption = 0
        pass

#------------------------------------------#


    def copyOfSystemCapability(self, capability):
        # a dictionary with each topic's capable devices for publishing to t
        self._system_capability = deepcopy(capability)

#------------------------------------------#


    def copyOfTopicTimeStamps(self, timestamps):
        # a dictionary with each topic's sense execution timestamp < T observation period
            # topic/1: [10,20,30...]
        self._experiment_timeline = deepcopy(timestamps)

#------------------------------------------#

    def saveDevicesTotalEnergyConsumed(self, random_energy_consumption):
        self._total_energy_consumption+= random_energy_consumption

#------------------------------------------#

    def resetTotalConsumption(self):
        self._total_energy_consumption = 0

#------------------------------------------#
        
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

#------------------------------------------#

    def random_algo(self):
        endAlgo = False
        while len(self._experiment_timeline.keys()) > 0:
            [newTask, newTaskTimeStamp] = self.findNextTask()
            
            # get a random device that is capable of performing the sensing task
            random_index = random.randrange(start=0, stop=len(self._system_capability[newTask]))
            publishing_mac = self._system_capability[newTask][random_index]
            energyIncrease = pub_c._publishers._devices[publishing_mac].energyIncrease(task_timestamp=newTaskTimeStamp)
            if energyIncrease + pub_c._publishers._devices[publishing_mac]._consumption >= pub_c._publishers._devices[publishing_mac]._battery:
                # save the current state
                print("last time = ",newTaskTimeStamp)
                endAlgo = True
                # exit algorithm
            else:
                pub_c._publishers._devices[publishing_mac].updateConsumption(energyIncrease)
                pub_c._publishers._devices[publishing_mac].addTimestamp(timestamp=newTaskTimeStamp)
                pub_c._publishers._devices[publishing_mac].setExecutions(new_value=pub_c._publishers._devices[publishing_mac].effectiveExecutions())
            if endAlgo:
                print("leaving random algo")
                return newTaskTimeStamp
        print("done with random algo")
        return None


