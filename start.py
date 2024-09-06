import argparse

parser = argparse.ArgumentParser()
#-u USERNAME -p PASSWORD -size 20000
parser.add_argument("-u", "--username",dest ="username", help="User name")
parser.add_argument("-p", "--password",dest = "password", help="Password")
parser.add_argument("-size", "--binsize",dest = "binsize", help="Size", type=int)

args = parser.parse_args()

# TODO: Determine optional + required flags for an experiment
    # config file path
    # experiment modes
        # energy consumption
        # system lifespan 
    # scheduler
        # MQTT-EES
        # Random
        # MQTT (lifespan only)

# Hold main execution

def main():
    print("Username {}, Password {} Size {}".format(args.username, args.password, args.binsize))

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
    #instantiateConfig()

    pass

if __name__ == "__main__":
    main()


        