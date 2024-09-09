from container.experiment_manager import Experiment_Manager
import threading
import time

exp_manager = Experiment_Manager()


def scheduler_cleanup():
    exp_manager.pub_c._publishers.resetUnits()
    exp_manager.pub_c._publishers.clearAllDeviceEnergyConsumption()

def round_cleanup():
    exp_manager.pub_c._publishers.clearUnits()
    exp_manager.pub_c._publishers.clearAllDeviceEnergyConsumption()
    exp_manager.topic_c.clearTopicDict()

def generateExperiment():
    exp_manager.experiment_setup()
    capability = exp_manager.createSystemCapability()
    ees_ob_period = random_ob_period = mqtt_ob_period = None
    if exp_manager.run_energy_exp:
        ees_ob_period = random_ob_period = mqtt_ob_period = exp_manager.config.DEFAULT_OB_PERIOD_MS

    elif exp_manager.run_lifespan_exp:
        ees_ob_period = exp_manager.config.EES_LIFESPAN_CONST
        random_ob_period = exp_manager.config.RANDOM_LIFESPAN_CONST
        mqtt_ob_period = exp_manager.config.MQTT_LIFESPAN_CONST
        # combine main_ees, main_mqtt, and main_random
    if "ees" in exp_manager.schedulers:
        exp_manager.create_ees(timestamps = exp_manager.topic_c.setupSenseTimestamps(    
                                    observation_period=ees_ob_period),
                                sys_capability=capability
                                )
    if "random" in exp_manager.schedulers:
        exp_manager.create_random(timestamps= exp_manager.topic_c.setupSenseTimestamps(
                                    observation_period=random_ob_period),
                                sys_capability=capability 
                                )
    if "mqtt" in exp_manager.schedulers:
        exp_manager.create_mqtt(timestamps=exp_manager.topic_c.setupSenseTimestamps(
                                    observation_period=mqtt_ob_period),
                                sys_capability=capability
                                )


def run_experiment():
    for round in range(exp_manager.config.NUM_ROUNDS):
        generateExperiment()
        if "ees" in exp_manager.schedulers:
            exp_manager.run_ees(round)
            scheduler_cleanup()
        if "random" in exp_manager.schedulers:
            exp_manager.run_random(round)
            scheduler_cleanup()
        if "mqtt" in exp_manager.schedulers:
            exp_manager.run_mqtt(round)
            scheduler_cleanup()
        round_cleanup()
        
   
    
if __name__ == "__main__":
    run_experiment()