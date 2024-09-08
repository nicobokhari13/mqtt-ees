from config.config_utils import ConfigUtils
from container.publisher import Publisher_Container
from container.subscriber import Subscriber_Container
from container.topic import Topic_Container
import random
from copy import deepcopy

# if lifespan is the mode, use default tail 

# if energy is the mode and vary are false, use default tail

class Experiment_Manager:

    # constructor
    def __init__(self):
        self.config = ConfigUtils._instance
        self.pub_c = Publisher_Container()
        self.sub_c = Subscriber_Container()
        self.topic_c = Topic_Container()
        self.results_folder_path = "results/"

        self.run_energy_exp = False
        self.run_lifespan_exp = False

        # experiment results defined by 
            # experiment mode
            # variable used
            # datetime experiment started

    def queueEnergyExperiment(self):
        self.run_energy_exp = True

    def queueLifespanExperiment(self):
        self.run_lifespan_exp = True

    def 

    def container_setup(self):
        self.topic_c.setupTopicStrings()
        self.sub_c.setUpSubscriberFrequencies()
        self.pub_c.setupDevices()

    # Precondition: all the topic strings are created
    def createSystemCapability(self):
        capability = {topic: [-1, []] for topic in self.topic_c._topic_dict.keys()}
        for topic in self.topic_c._topic_dict.keys(): # for every topic
            for device in self.pub_c._publishers._devices.values(): # find the device
                if device.capableOfPublishing(topic):
                    capability[topic][1].append(device._device_mac)
        return capability
        # different for every round

    #------------------------------------------#

    def setup_exp_vary_pub(self):
        exp_num_pub = random.randint(self.config.PUBLISHER_MIN, self.config.PUBLISHER_MAX)
        self.pub_c.setTotalDevices(num_devs=exp_num_pub)
        self.topic_c.setTotalTopic(num_topics=self.config.DEFAULT_TOPIC)
        self.sub_c.setTotalSubs(num_subs=self.config.DEFAULT_SUBSCRIBER)

        self.container_setup()


    #------------------------------------------#


    def setup_exp_vary_sub(self):
        exp_num_subs = random.randint(self.config.SUBSCRIBER_MIN, self.config.SUBSCRIBER_MAX)
        self.pub_c.setTotalDevices(num_devs=self.config.DEFAULT_PUBLISHER)
        self.topic_c.setTotalTopic(num_topics=self.config.DEFAULT_TOPIC)
        self.sub_c.setTotalSubs(num_subs=exp_num_subs)

        self.container_setup()

    #------------------------------------------#

    def setup_exp_vary_topic(self):
        exp_num_topics = random.randint(self.config.TOPIC_MIN, self.config.TOPIC_MAX)
        self.pub_c.setTotalDevices(num_devs=self.config.DEFAULT_PUBLISHER)
        self.sub_c.setTotalSubs(num_subs=self.config.DEFAULT_SUBSCRIBER)
        self.topic_c.setTotalTopic(num_topics=exp_num_topics)

        self.container_setup()

    #------------------------------------------#

    def setup_default(self):
        self.pub_c.setTotalDevices(num_devs=self.config.DEFAULT_PUBLISHER)
        self.sub_c.setTotalSubs(num_subs=self.config.DEFAULT_SUBSCRIBER)
        self.topic_c.setTotalTopic(num_topics=self.config.DEFAULT_TOPIC)
        
        self.container_setup()

    #------------------------------------------#

    # performed once before the rounds start
    def experiment_setup(self):
        # based on the vary_xxx config settings, begin setup functions for the containers
        if self.config._vary_pubs:
            print("varying publishers")
            self.setup_exp_vary_pub()
        elif self.config._vary_subs:
            print("varying subscribers")
            self.setup_exp_vary_sub()        
        elif self.config._vary_topics:
            print("varying topics")
            self.setup_exp_vary_topic()
        else:
            print("using defaults")
            self.setup_default()
        print("setting up timestamps")

        timestamps = None
        # if the experiment mode is lifespan, 
            # the timestamps are different for each scheduler
            # for algorithm in schedulers
                # if algo == ees
                    # period = config.consant.ees
                # elif algo == mqtt
                    # period = config.constant.mqtt
                # elif algo == random
                    # period = config.constant.random
                # timestamps = topic.setupSenseTimestamps(self, period)


        self.topic_c.setupSenseTimestamps()
        global system_capability 
        print("setting up system capability")
        system_capability = self.createSystemCapability()

        
    def run_ees(self):
        pass

    def run_random(self):
        pass

    def run_mqtt(self):
        pass

    
