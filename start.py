from config.config_mgmt import *
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
    # get command line input

# based on command line input, modify experiment modes
    # experiment mode (lifespan or energy usage)
    # schedulers
        # random
        # mqtt-ees
        # mqtt
    # experiment manager set up
    # TODO: Whiteboard out start.py input parameters impact experiment round properties (json at runtime) 
        # what experiment_manager may use in
    instantiateConfig()

    pass

if __name__ == "__main__":
    main()


        