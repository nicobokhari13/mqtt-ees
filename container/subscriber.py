import random
from container.topic import Topic_Container

topic_c = Topic_Container()

class Subscriber_Container:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance
    
    def __init__(self) -> None:
        self._total_subs = 0
        pass

    def setDefaultNumSubs(self, default_num_subs):
        self._default_num_subs = default_num_subs

    def setFrequencyMinMax(self, min, max):
        self._lat_qos_min = min
        self._lat_qos_max = max

    # Precondition: Topics in Topic Container are created beforehand, defaults are set
    def setUpSubscriberFrequencies(self, num_subs):
        if num_subs == 0:
            print(f"setting default subscribers {self._default_num_subs}")
            num_subs = self._default_num_subs
        self._total_subs = num_subs
        print(f"creating {num_subs} subscribers")
        for sub in range(num_subs):
            num_subscriptions = random.randint(a=1, b=topic_c._total_topics)
            subscriptions = random.sample(population=topic_c._topic_dict.keys(), k=num_subscriptions)
            for subscription in subscriptions:
                sub_lat_qos = random.randint(a=self._lat_qos_min, b=self._lat_qos_max)
                topic_c.updateFrequency(topic_changed=subscription, sub_lat=sub_lat_qos)
        self.ensureTopicCoverage()


    def ensureTopicCoverage(self):
        for topic in topic_c._topic_dict.keys():
            if topic_c._topic_dict[topic] < 0:
                topic_c._topic_dict[topic] = random.randint(a=self._lat_qos_min, b=self._lat_qos_max)
