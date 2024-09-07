import argparse
from config.config_mgmt import *
parser = argparse.ArgumentParser()

#-config for config file path
config_help_string =    """
                        A valid file path to a configuration inii file. 
                        See example configuration in config_example.ini
                        """

experiment_mode_help_string =    """
                            The experiment modes supported track different metrics, and result in different results files.
                            The following are the only options
                            lifespan, energy
                            """

#-sched for schedulers
sched_help_string =   """
                Comma delimited list of schedulers to run in experiment. \n
                Values include: mqttees,random,mqtt
                """

parser.add_argument("-config", "--configuration",dest ="config_file", help=config_help_string, type=str)
parser.add_argument("-mode", "--experimentmode",dest ="experiment_mode", help=experiment_mode_help_string, type=str)
parser.add_argument("-scheds", "--schedulers",dest ="schedulers", help=sched_help_string, type=str)

args = parser.parse_args()


# Hold main execution

def main():
    config_file = args.config_file
    experiment_mode = args.experiment_mode.split(",")
    schedulers = args.schedulers.split(",")

    print(f"config file path: {config_file , type(config_file)}")
    print(f"experiment mode: {experiment_mode, type(experiment_mode)}")
    print(f"using schedulders : {schedulers, type(schedulers)}") 
    
    if "energy" in experiment_mode and "mqtt" in schedulers: 
        print("cannot schedule mqtt base protocol with energy consumption simulation. Use ees and/or random scheduling")
        exit()

    instantiateConfig(configuration_file=config_file)
    config_status = verifyConfig()
    if config_status == CONFIG_INVALID or config_status is None: 
        print("configuration is invalid or the Configuration File was not created")
        exit()
    else: # configuration is valid, ready to start experiment
        # create experiment manager

        pass


if __name__ == "__main__":
    main()


        