import configparser
from config_monitor import * 

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

    # RANGES
    topic_range = list(map(int,self._config.get("RANGES", "topic_range").split(",")))
    sub_range = list(map(int,self._config.get("RANGES", "sub_range").split(",")))
    pub_range = list(map(int,self._config.get("RANGES", "pub_range").split(",")))

    tail_window_range = list(map(int,self._config.get("RANGES", "tail_window_range").split(",")))
        # get the list of tail window values availale to simulate
    freq_ms_range = list(map(int, self._config.get("RANGES", "freq_ms_range").split(",")))
        # get the min and max values of sensing frequencies
    
    # Variables
    self.TOPIC_MIN = topic_range[0]
    self.TOPIC_MAX = topic_range[1]

    self.SUBSCRIBER_MIN = sub_range[0]
    self.SUBSCRIBER_MAX = sub_range[1]

    self.PUBSCRIBER_MIN = pub_range[0]
    self.PUBSCRIBER_MAX = pub_range[1]

    self.FREQ_MS_MIN = freq_ms_range[0]
    self.FREQ_MS_MAX = freq_ms_range[1]

        # DEFAULTS
    self.DEFAULT_PUBSCRIBER = int(self._config.get("DEFAULTS", "def_num_pubs"))
    self.DEFAULT_SUBSCRIBER = int(self._config.get("DEFAULTS", "def_num_subs"))
    self.DEFAULT_TOPIC = int(self._config.get("DEFAULTS", "def_num_topics")) 

    # Energies
    self.SENSE_ENERGY = float(self._config.get("CONSTANTS", "sense_energy"))
    self.COMM_ENERGY = float(self._config.get("CONSTANTS", "comm_energy"))





    # CONSTANTS 

    # Observation Period
    self.OBSERVATION_PERIOD_MILISEC = int(self._config.get("CONSTANTS", "ob_period"))

    # Tail Window (ms)
    # self._tail_window_ms = int(self._config.get("CONSTANTS", "tail_window _ms"))
    # TODO; move tail window use to experiment and triggered via bash script flags
    



   


def validateConfigValues(self):
    # the monitor provides the raw logic
    # config utils actully performs actions to stop the experiment if config monitor returns False
    pass

# TODO : print config status at the beginng of each experiment round

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