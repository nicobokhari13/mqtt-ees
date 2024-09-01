from config_monitor import * 
from config_utils import * 


def instantiateConfig(configuration_file : str):

    configuration = ConfigUtils()
    configuration.saveFilePath(configuration_file)
    configuration.setConstants()


def verifyConfig():

    if(ConfigUtils._instance is None) or (ConfigMonitor._instance is None):
        return None
    configuration = ConfigUtils()
    monitor = ConfigMonitor()
    if  monitor.validConfigMinMaxRange(configuration.TOPIC_MIN, configuration.TOPIC_MAX) and \
        monitor.validConfigMinMaxRange(configuration.SUBSCRIBER_MIN, configuration.SUBSCRIBER_MAX) and \
        monitor.validConfigMinMaxRange(configuration.PUBLISHER_MIN, configuration.PUBLISHER_MAX) and \
        monitor.validConfigMinMaxRange(configuration.FREQ_MS_MIN, configuration.FREQ_MS_MAX) and \
        monitor.nonZero(value = configuration.NUM_ROUNDS) and \
        monitor.nonZero(value = configuration.OBSERVATION_PERIOD_MS) and \
        monitor.nonZero(value=configuration.DEFAULT_TAIL_WINDOW_MS) and  \
        (0 not in configuration.TAIL_WINDOW_RANGE):

        return CONFIG_VALID
    else:
        return CONFIG_INVALID
            
