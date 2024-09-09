from .config_monitor import ConfigMonitor
from .config_utils import ConfigUtils

def verifyConfig():

    if(ConfigUtils._instance is None):
        return None
    configuration = ConfigUtils()
    monitor = ConfigMonitor()
    if  monitor.validConfigMinMaxRange(configuration.TOPIC_MIN, configuration.TOPIC_MAX) and \
        monitor.validConfigMinMaxRange(configuration.SUBSCRIBER_MIN, configuration.SUBSCRIBER_MAX) and \
        monitor.validConfigMinMaxRange(configuration.PUBLISHER_MIN, configuration.PUBLISHER_MAX) and \
        monitor.validConfigMinMaxRange(configuration.FREQ_MS_MIN, configuration.FREQ_MS_MAX) and \
        monitor.nonZero(value = configuration.NUM_ROUNDS) and \
        monitor.nonZero(value = configuration.DEFAULT_OB_PERIOD_MS) and \
        monitor.nonZero(value=configuration.DEFAULT_TAIL_WINDOW_MS):
        
        return ConfigMonitor.CONFIG_VALID
    else:
        return ConfigMonitor.CONFIG_INVALID
            
