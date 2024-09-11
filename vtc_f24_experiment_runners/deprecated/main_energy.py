from datetime import datetime
from container.publisher import Publisher_Container
from container.topic import Topic_Container
from container.subscriber import Subscriber_Container
import random
import sys
import csv
from schedulers.mqtt_ees import MQTTEES
from schedulers.random_algo import Random
from schedulers.mqtt_algo import Standard

#------------------------------------------#
# create capability matrix
    # dictionary with
        # key = topic
        # value = tuple (index of device publishing to key topic, [list of all devices capable of publishing to topic])
system_capability = {}

#------------------------------------------#

# Precondition: all the topic strings are created
def createSystemCapability():
    capability = {topic: [-1, []] for topic in topic_c._topic_dict.keys()}
    for topic in topic_c._topic_dict.keys(): # for every topic
        for device in pub_c._publishers._devices.values(): # find the device
            if device.capableOfPublishing(topic):
                capability[topic][1].append(device._device_mac)
    return capability

#------------------------------------------#


def setup_exp_vary_pub():
    exp_num_pub = random.randint(3, configuration._max_pubs)
    topic_c.setupTopicStrings(numTopics=0)
    sub_c.setUpSubscriberFrequencies(num_subs=0)
    pub_c.setupDevices(num_pubs=exp_num_pub)

#------------------------------------------#


def setup_exp_vary_sub():
    exp_num_subs = random.randint(3, configuration._max_subs)
    topic_c.setupTopicStrings(numTopics=0)
    sub_c.setUpSubscriberFrequencies(num_subs=exp_num_subs)
    pub_c.setupDevices(num_pubs=0)

#------------------------------------------#


def setup_exp_vary_topic():
    exp_num_topics = random.randint(3, configuration._max_topics)
    topic_c.setupTopicStrings(numTopics=exp_num_topics)
    sub_c.setUpSubscriberFrequencies(num_subs=0)
    pub_c.setupDevices(num_pubs=0)


#------------------------------------------#

def setup_default():
    topic_c.setupTopicStrings(numTopics=0)
    sub_c.setUpSubscriberFrequencies(num_subs=0)
    pub_c.setupDevices(num_pubs=0)

#------------------------------------------#


# performed once before the rounds start
def experiment_setup():
    # based on the vary_xxx config settings, begin setup functions for the containers
    if configuration._vary_pubs:
        print("varying publishers")
        setup_exp_vary_pub()
    elif configuration._vary_subs:
        print("varying subscribers")
        setup_exp_vary_sub()        
    elif configuration._vary_topics:
        print("varying topics")
        setup_exp_vary_topic()
    else:
        print("using defaults")
        print("varying threshold")
        setup_default()
        #sys.exit()
    print("setting up timestamps")
    topic_c.setupSenseTimestamps()
    global system_capability 
    print("setting up system capability")
    system_capability = createSystemCapability()
    #print(system_capability)

#------------------------------------------#


# CSV Format for all files
    # algo_name, num_round, num_topic, num_pubs, num_subs, total_energy_consumption
def saveResults(algo_name:str, num_round, num_topic, num_pubs, num_subs, total_energy_consumption, time_end):
    if configuration._vary_pubs:
        file_path = file_paths["pub_path"] + filename + "pub"
    elif configuration._vary_subs:
        file_path = file_paths["sub_path"] + filename + "sub"
    elif configuration._vary_topics:
        file_path = file_paths["topic_path"] + filename + "topic"
    else:
        file_path = "results_lasting_time/" + filename + "obperiod_" + str(configuration.OBSERVATION_PERIOD_MILISEC) 
        #file_path = file_paths["threshold_path"] + filename + "thresh_" + str(configuration._THRESHOLD_WINDOW) 
    file_path = file_path + ".csv"
    data = [algo_name, time_end, num_round, num_topic, num_pubs, num_subs, total_energy_consumption]
    for device in pub_c._publishers._devices.keys():
        data.append(pub_c._publishers._devices[device]._consumption)
    with open(file_path, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(data)

#------------------------------------------#


def getConsumption():
    totalConsumption = 0
    for deviceMac in pub_c._publishers._devices.keys():
        totalConsumption += pub_c._publishers._devices[deviceMac]._consumption
    return totalConsumption

#------------------------------------------#


def main():
    # create algo objects

    cc = MQTTEES()
    rand = Random()
    mqtt = Standard()
    global system_capability
    for round in range(configuration._sim_rounds):
        print("round number: ", round)
        # set up experiment
        experiment_setup()
        # set system capability and timestamps for algorithms

        rand.copyOfSystemCapability(system_capability)
        rand.copyOfTopicTimeStamps()    
        cc.copyOfSystemCapability(system_capability)
        cc.copyOfTopicTimeStamps()
        mqtt.copyOfSystemCapability(system_capability)
        mqtt.copyOfTopicTimeStamps()

# SIMULATE ALGORITHMS
# ==================== Random ====================
        timeEnd = rand.random_algo()
        if timeEnd is None:
            timeEnd = "None"
        # # # save the total energy consumption
        # # #pub_c._devices.calculateTotalEnergyConsumption()
        # # #random_energy_consumption = pub_c._devices._all_devices_energy_consumption
        # # #random.saveDevicesTotalEnergyConsumed(round_energy_consumption=rr_energy_consumption)
        totalConsumption = getConsumption()
        saveResults(algo_name=rand._algo_name, time_end=timeEnd, num_round=round, num_topic=topic_c._total_topics, num_pubs=pub_c._total_devices, num_subs=sub_c._total_subs, total_energy_consumption=totalConsumption)
        
        # # # reset experiment for next algorithm
        pub_c._publishers.resetUnits()
        pub_c._publishers.clearAllDeviceEnergyConsumption()
# ==================== MQTT ==================== 
        mqtt.mqtt_algo()
        totalConsumption = getConsumption()
        saveResults(algo_name=mqtt._algo_name, num_round=round, num_topic=topic_c._total_topics, num_pubs=pub_c._total_devices, num_subs=sub_c._total_subs, total_energy_consumption=totalConsumption)
        pub_c._publishers.resetUnits()
        pub_c._publishers.clearAllDeviceEnergyConsumption()
# ==================== MQTT-EES ====================
        timeEnd = cc.mqttees_algo()
        if timeEnd is None:
            timeEnd = "None"
        totalConsumption = getConsumption()
        saveResults(algo_name=cc._algo_name, time_end=timeEnd, num_round=round, num_topic=topic_c._total_topics, num_pubs=pub_c._total_devices, num_subs=sub_c._total_subs, total_energy_consumption=totalConsumption)
        pub_c._publishers.resetUnits()
        pub_c._publishers.clearAllDeviceEnergyConsumption()
        # # save the total energy consumption
        # #pub_c._devices.calculateTotalEnergyConsumption()
        # #cc_energy_consumption = pub_c._devices._all_devices_energy_consumption
        # #cc.saveDevicesTotalEnergyConsumed(cc_energy_consumption)
        # #saveResults(algo_name=cc._algo_name, num_round=round, num_topic=topic_c._total_topics, num_pubs=pub_c._total_devices, num_subs=sub_c._total_subs, total_energy_consumption=cc_energy_consumption)
        # pub_c._devices.resetUnits()
        # pub_c._devices.clearAllDeviceEnergyConsumption()

# ==================== END OF SIMULATED ROUND ====================
        # end of round clean up
        pub_c._publishers.clearUnits()
        pub_c._publishers.clearAllDeviceEnergyConsumption()
        topic_c.clearTopicDict()
        
        
# ==================== END OF SIMULATION====================

    print(last_msg)
    
# acquire stats

    # after all the rounds, calculate the average system energy consumption per round
    # rr_avg_energy_consumption = rr._total_energy_consumption / configuration._sim_rounds
    # cc_avg_energy_consumption = cc._total_energy_consumption / configuration._sim_rounds
    # saveResults(algo_name=rr._algo_name, avg_energy_consumption=rr_avg_energy_consumption)
    # saveResults(algo_name=cc._algo_name, avg_energy_consumption=cc_avg_energy_consumption)


if __name__ == "__main__":
    main()
