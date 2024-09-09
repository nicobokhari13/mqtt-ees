from config.config_utils import ConfigUtils
# variable containers
from container.publisher import Publisher_Container
from container.subscriber import Subscriber_Container
from container.topic import Topic_Container
# schedulers
from schedulers.mqtt_algo import Standard
from schedulers.random_algo import Random
from schedulers.mqtt_ees import MQTTEES
import random
import csv
from copy import deepcopy
from datetime import datetime

# if lifespan is the mode, use default tail 

# if energy is the mode and vary are false, use default tail

class Experiment_Manager:
    _instance = None
    
    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance
    # constructor
    def __init__(self):
        self.config = ConfigUtils._instance
        self.pub_c = Publisher_Container()
        self.sub_c = Subscriber_Container()
        self.topic_c = Topic_Container()
        date_now = datetime.now().replace(microsecond=0)
        date_string = str(date_now)
        date_string = date_string.replace(":","-")
        date_string = date_string.replace(" ", "_")
        self.results_folder_path = "results_" + date_string

        self.run_energy_exp = False
        self.run_lifespan_exp = False

        self.schedulers = None
        self.results_csv_file_paths = {}
        # experiment results defined by 
            # experiment mode
            # variable used
            # datetime experiment started

    def saveSchedulers(self, scheds) :
        self.schedulers = scheds

    def queueEnergyExperiment(self):
        self.run_energy_exp = True

    def queueLifespanExperiment(self):
        self.run_lifespan_exp = True

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
        # based on the    config settings, begin setup functions for the containers
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

    def createSystemCapability(self):
        capability = {topic: [-1, []] for topic in self.topic_c._topic_dict.keys()}
        for topic in self.topic_c._topic_dict.keys(): # for every topic
            for device in self.pub_c._publishers._devices.values(): # find the device
                if device.capableOfPublishing(topic):
                    capability[topic][1].append(device._device_mac)
        return capability
    
    def createTimestamps(self, observation_period):
        return self.topic_c.setupSenseTimestamps(observation_period)
    

# CSV Format for all files 
    # algo_name, num_round, num_topic, num_pubs, num_subs, total_energy_consumption
    def saveResults(self, algo_name, num_round, num_topic, num_pubs, num_subs, total_energy_consumption, time_end):
        if self.run_energy_exp:
            experiment_mode = "energy"
        elif self.run_lifespan_exp:
            experiment_mode = "lifespan"

        if self.config._vary_pubs:
            file_path = self.results_csv_file_paths[experiment_mode] + "_pubs"
        elif self.config._vary_subs:
            file_path = self.results_csv_file_paths[experiment_mode] + "_subs"
        elif self.config._vary_topics:
            file_path = self.results_csv_file_paths[experiment_mode] + "_topics"
        else: 
            if experiment_mode == "energy":
                file_path = self.results_csv_file_paths[experiment_mode] + "_tailwindow"
            elif experiment_mode == "lifespan":
                file_path = self.results_csv_file_paths[experiment_mode] + "_defaults"
            #file_path = file_paths["threshold_path"] + filename + "thresh_" + str(configuration._THRESHOLD_WINDOW) 
        file_path = file_path + ".csv"
        data = [algo_name, time_end, num_round, num_topic, num_pubs, num_subs, total_energy_consumption]
        for device in self.pub_c._publishers._devices.keys():
            data.append(self.pub_c._publishers._devices[device]._consumption)
        with open(file_path, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(data)

        

    def getEnergyConsumption(self):
        totalConsumption = 0
        for deviceMac in self.pub_c._publishers._devices.keys():
            totalConsumption += self.pub_c._publishers._devices[deviceMac]._consumption
        return totalConsumption
    
    def collectResults(self, shutdown_timestamp, algo, round_num):
        totalConsumption = self.getEnergyConsumption()
        self.saveResults(algo_name=algo, 
                         time_end=shutdown_timestamp,
                         num_round=round_num, 
                         num_topic=self.topic_c._total_topics, 
                         num_pubs=self.pub_c._total_devices, 
                         num_subs=self.sub_c._total_subs,
                         total_energy_consumption=totalConsumption
                        )

    def create_ees(self, timestamps, sys_capability):
        ees_schedule = MQTTEES()
        ees_schedule.copyOfTopicTimeStamps(timestamps)
        ees_schedule.copyOfSystemCapability(sys_capability)

    def create_random(self, timestamps, sys_capability):
        random_schedule = Random()
        random_schedule.copyOfTopicTimeStamps(timestamps)
        random_schedule.copyOfSystemCapability(sys_capability)

    def create_mqtt(self, timestamps, sys_capability):
        mqtt_schedule = Standard()
        mqtt_schedule.copyOfTopicTimeStamps(timestamps)
        mqtt_schedule.copyOfSystemCapability(sys_capability)

    def run_ees(self, round_num):
        ees_schedule = MQTTEES()
        shutdown_timestamp = ees_schedule.mqttees_algo()
        if shutdown_timestamp is None:
            shutdown_timestamp = "NA"
        self.collectResults(shutdown_timestamp=shutdown_timestamp, algo="ees", round_num=round_num)

    def run_random(self, round_num):
        random_schedule = Random()
        shutdown_timestamp = random_schedule.random_algo()
        if shutdown_timestamp is None:
            shutdown_timestamp = "NA"
        self.collectResults(shutdown_timestamp=shutdown_timestamp, algo="random", round_num=round_num)
        

    def run_mqtt(self, round_num):
        mqtt_schedule = Standard()
        shutdown_timestamp  = mqtt_schedule.mqtt_algo()
        if shutdown_timestamp is None:
            shutdown_timestamp = "NA"
        self.collectResults(shutdown_timestamp=shutdown_timestamp, algo="mqtt", round_num=round_num)

        

            
            
            


        
    def run_random(self):
        random_schedule = Random()
    
    def run_mqtt(self):
        mqtt_schedule = Standard()
        

