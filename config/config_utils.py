import configparser
from config_monitor import ConfigMonitor

class ConfigUtils:
    ### Singleton Instance
    _instance = None
    
    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        self._config = configparser.ConfigParser()
        self._monitor = ConfigMonitor()

#------------------------------------------#
# PRECONDITION:
# PARAMETERS:
#

def saveFilePath(self, configFilePath):
    self._CONFIG_FILE_PATH = configFilePath
    pass 

def setConstants(self):
    self._config.read(self._CONFIG_FILE_PATH)
    pass

def validateConfigValues(self):
    # the monitor provides the raw logic
    # config utils actully performs actions to 
    pass

# POSTCONDITION:
#


#------------------------------------------#

    # PRECONDITION: ConfigUtils already initialized
    # PARAMETERS:
        # configFilePath : a valid file path in the project directory ./config
    # POSTCONDITION: All of instance's variables set to constants defined in parameter file path
    def setConstants(self, configFilePath):
        self._CONFIG_FILE_PATH = configFilePath
        self._config.read(self._CONFIG_FILE_PATH)
        # Observation Period
        self.OBSERVATION_PERIOD_MILISEC = int(self._config.get("CONSTANTS", "ob_period"))
        # Frequency Ranges
        self.MIN_FREQ_MS = int(self._config.get("CONSTANTS", "min_freq_ms"))
        self.MAX_FREQ_MS = int(self._config.get("CONSTANTS", "max_freq_ms"))
        # Tail Window (ms)
        self._tail_window_ms = int(self._config.get("CONSTANTS", "tail_window _ms"))
        # Energies
        self._sense_energy = float(self._config.get("CONSTANTS", "sense_energy"))
        self._comm_energy = float(self._config.get("CONSTANTS", "comm_energy"))
        # Sim Rounds
        self._sim_rounds = int(self._config.get("CONSTANTS","num_rounds"))
        #Max Variable Values
        self._max_pubs = int(self._config.get("VARS", "max_pubs"))
        self._max_subs = int(self._config.get("VARS", "max_subs"))
        self._max_topics = int(self._config.get("VARS", "max_topics"))
        # Define Variables
        self._vary_pubs = self._config.get("VARS", "vary_pubs") == "true"
        self._vary_subs = self._config.get("VARS", "vary_subs") == "true"
        self._vary_topics = self._config.get("VARS", "vary_topics") == "true"
        # Define Defaults 
        self._default_num_pubs = int(self._config.get("DEFAULTS", "def_num_pubs"))
        self._default_num_subs = int(self._config.get("DEFAULTS", "def_num_subs"))
        self._default_num_topics = int(self._config.get("DEFAULTS", "def_num_topics"))



#------------------------------------------#
# PRECONDITION:
# PARAMETERS:
#
# POSTCONDITION:
#