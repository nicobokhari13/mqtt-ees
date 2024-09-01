from config_monitor import * 
from config_utils import * 


def instantiateConfig(configuration_file : str):
    # create Config Utils
    configuration = ConfigUtils()
    monitor = ConfigMonitor()


def verifyConfig():
    if(ConfigUtils._instance is None) or (ConfigMonitor._instance is None):
        pass
