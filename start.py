from config.config_utils import ConfigUtils
from datetime import datetime
from container.publisher import Publisher_Container
from container.topic import Topic_Container
from container.subscriber import Subscriber_Container
import random
import sys
import csv
from schedulers.mqtt_cc import MQTTCC
# Hold main execution

def main():
    print("hello world")
    pass

if __name__ == "__main__":
    main()
# command line input

# based on command line input, modify experiment modes
    # experiment mode
    # schedulers
        # random
        # mqtt-ees
        # mqtt
    # all via flags -> change config file for scheduler/experiment specific info
        # for example, publishers taking the minimum frequency from all subscriptions on a topic
        # turn on topic subscription frequency persistence
            # when a subscriber leaves and the frequency they required was the minimum, 
            # update the minimum -> update the frequency of the topic


# experiment manager set up

    # config setup
    
    # try custom exception handling if config is incompatible
    
# 