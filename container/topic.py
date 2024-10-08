from copy import deepcopy
from config.config_utils import ConfigUtils
config_file = ConfigUtils()

class Topic_Container:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance
    
    def __init__(self) -> None:
        self._total_topics = 0

    def setTotalTopic(self, num_topics):
        self._total_topics = num_topics

    def setupTopicStrings(self):
        print(f"creating {self._total_topics} topics")
        self._topic_dict = dict()
        topic_list = self.generateTopics()
        for topic in topic_list:
            self._topic_dict[topic] = -1 # default until changed

    def generateTopics(self):
        self.clearTopicDict()
        topic_list = [f"topic/{i}" for i in range(self._total_topics)]
        #print(topic_list)
        return topic_list
    
    def updateFrequency(self, topic_changed, sub_lat):
        if self._topic_dict[topic_changed] < 0 or self._topic_dict[topic_changed] > sub_lat:
            self._topic_dict[topic_changed] = sub_lat

    def unusedTopics(self):
        if -1 in self._topic_dict.values():
            return True
        else: 
            return False
        
    def clearTopicDict(self):
        self._topic_dict.clear()
    
    # Precondition: all topics are created, all subscribers created
        # all frequencies assigned to all topics
    # Postcondition: all_sense_timestamps is a dictionary where 
        # key: topic from topic_dict
        # value: list of frequency timestamps from 0 - T observation period 
        # this object is copied by all schedulers, need deepcopy for each
        # only created once per round
    def setupSenseTimestamps(self, observation_period):
        all_sense_timestamps = {}
        for topic in self._topic_dict.keys():
            freq = self._topic_dict[topic]
            multiples = list(range(0, observation_period + 1, freq))
            # at the end of the loop timestamp_list has all of freq's timestamps < T
            all_sense_timestamps[topic] = deepcopy(multiples)
            # example, if topic/1 publishes every 10ms, then topic/1: [10,20,30...]
        return all_sense_timestamps
    
    def resetSenseTimestamps(self):
        self._all_sense_timestamps.clear() 
    