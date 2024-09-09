from container.experiment_manager import Experiment_Manager

exp_manager = Experiment_Manager()

exp_manager.experiment_setup()

def getConsumption():
    totalConsumption = 0
    for deviceMac in exp_manager.pub_c._publishers._devices.keys():
        totalConsumption += exp_manager.pub_c._publishers._devices[deviceMac]._consumption
    return totalConsumption


def main():
    capability = exp_manager.createSystemCapability()
    if exp_manager.run_lifespan_exp:
        # combine main_ees, main_mqtt, and main_random
        if "ees" in exp_manager.schedulers:

            exp_manager.run_ees(
                timestamps = 
                    exp_manager.createTimestamps(observation_period= 
                                                    exp_manager.config.EES_LIFESPAN_CONST),
                sys_capability = capability
            )
        if "random" in exp_manager.schedulers:

            exp_manager.run_random(
                timestamps = 
                    exp_manager.createTimestamps(observation_period=
                                                    exp_manager.config.RANDOM_LIFESPAN_CONST
                                                 ),
                sys_capability = capability
            )

        if "mqtt" in exp_manager.schedulers:

            exp_manager.run_mqtt(
                timestamps = 
                    exp_manager.createTimestamps(observation_period=
                                                    exp_manager.config.MQTT_LIFESPAN_CONST
                                                ),
                sys_capability = capability
            )
            
    if exp_manager.run_energy_exp:
        # same as main_runner

if __name__ == "__main__":
    main()