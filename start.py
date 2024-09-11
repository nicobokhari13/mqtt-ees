import argparse
import os
from config import *
from container.experiment_manager import Experiment_Manager
from vtc_f24_experiment_runners import main_runner

# ------------------------------------------------------------------
# [Nico Bokhari] start.py
#          The execution script for a Python simulation measuring MQTT-EES,
#          a task orchestration algorithm for energy efficient MQTT systems
# ------------------------------------------------------------------

# help strings for the script flags
config_help_string =    """
                        A valid file path to a configuration inii file. 
                        See example configuration in config_example.ini
                        """

experiment_mode_help_string =    """
                            The experiment modes supported track different metrics, and result in different results files.
                            The following are the only options:
                            lifespan, energy
                            """

sched_help_string =   """
                Comma delimited list of schedulers to run in experiment. \n
                Values include: mqttees,random,mqtt
                """

# flag parser
parser = argparse.ArgumentParser()
parser.add_argument("-config", "--configuration",dest ="config_file", help=config_help_string, type=str)
parser.add_argument("-mode", "--experimentmode",dest ="experiment_mode", help=experiment_mode_help_string, type=str)
parser.add_argument("-scheds", "--schedulers",dest ="schedulers", help=sched_help_string, type=str)

# script arguments stored as strings 
# the destination variable is the same name as the "dest" parameter in parser.add_argument
args = parser.parse_args()


# Hold main execution

def main():
    config_file = args.config_file
    experiment_mode = args.experiment_mode
    schedulers = args.schedulers.split(",")
    
    script_dir = os.path.dirname(os.path.abspath(__file__))

    print(f"config file path: {config_file , type(config_file)}")
    print(f"experiment mode: {experiment_mode, type(experiment_mode)}")
    print(f"using schedulders : {schedulers, type(schedulers)}") 
    
    if experiment_mode == 'energy' and "mqtt" in schedulers: 
        print("cannot schedule mqtt base protocol with energy consumption simulation. Use ees and/or random scheduling")
        exit()

    # process config file 
    config = ConfigUtils()
    config.instantiateConfig(config_file)
    config_status = verifyConfig()
    if config_status == ConfigMonitor.CONFIG_INVALID or config_status is None: 
        print("configuration is invalid or the Configuration File was not created")
        exit()
    
    print("configuration is ready, starting experiment setup")
    # configuration is valid, ready to start experiment
    
    exp_manager = Experiment_Manager()
        # queue the experiment modes inputted from flags
    if experiment_mode == "lifespan":
        exp_manager.queueLifespanExperiment()
        
    if experiment_mode == "energy":
        exp_manager.queueEnergyExperiment()
            
    exp_manager.saveSchedulers(schedulers)
        
    exp_manager.setResultsDirectoryPaths(script_dir, experiment_mode)


if __name__ == "__main__":
    main()
    main_runner.run_experiment()
    
    


        