import configparser

class ConfigUtils:
    ### Singleton Instance
    _instance = None
    
    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        self._config = configparser.ConfigParser()

#------------------------------------------#
# PRECONDITION:
# PARAMETERS:
#

    def saveFilePath(self, configFilePath):
        self._CONFIG_FILE_PATH = configFilePath
        pass 

    def setConstants(self):
        self._config.read(self._CONFIG_FILE_PATH)

        # VARS

        self.VARIABLES = {
            "publishers" : self._config.getboolean("VARS", "vary_pubs"), 
            "subscribers" : self._config.getboolean("VARS", "vary_subs"), 
            "topics" : self._config.getboolean("VARS", "vary_topics"), 
            "tail_window_ms" : self._config.getboolean("VARS", "vary_tail_window_ms"), 
        }


        # RANGES
        topic_range = list(map(int,self._config.get("RANGES", "topic_range").split(",")))
        sub_range = list(map(int,self._config.get("RANGES", "sub_range").split(",")))
        pub_range = list(map(int,self._config.get("RANGES", "pub_range").split(",")))
        freq_ms_range = list(map(int, self._config.get("RANGES", "freq_ms_range").split(",")))
            # get the min and max values of sensing frequencies
        
        self.TAIL_WINDOW_RANGE = list(map(int,self._config.get("RANGES", "tail_window_range").split(",")))
            # get the list of tail window values availale to simulate

            # get the min and max values of each range
        self.TOPIC_MIN = topic_range[0]
        self.TOPIC_MAX = topic_range[1]

        self.SUBSCRIBER_MIN = sub_range[0]
        self.SUBSCRIBER_MAX = sub_range[1]

        self.PUBLISHER_MIN = pub_range[0]
        self.PUBLISHER_MAX = pub_range[1]

        self.FREQ_MS_MIN = freq_ms_range[0]
        self.FREQ_MS_MAX = freq_ms_range[1]

        # DEFAULTS
        self.DEFAULT_PUBSCRIBER = int(self._config.get("DEFAULTS", "def_val_pubs"))
        self.DEFAULT_SUBSCRIBER = int(self._config.get("DEFAULTS", "def_val_subs"))
        self.DEFAULT_TOPIC = int(self._config.get("DEFAULTS", "def_val_topics")) 
        self.DEFAULT_TAIL_WINDOW_MS = int(self._config.get("DEFAULTS", "def_val_tail_window_ms"))

        # create a dictionary with key:value such that value = not(self.VARIABLES[key])
        self.USE_DEFAULT = dict()
        for key in self.VARIABLES.keys():
            self.USE_DEFAULT[key] = not(self.VARIABLES[key])

        # CONSTANTS 
        self.SENSE_ENERGY = float(self._config.get("CONSTANTS", "sense_energy"))
        self.COMM_ENERGY = float(self._config.get("CONSTANTS", "comm_energy"))
        self.NUM_ROUNDS = int(self._config.get("CONSTANTS", "num_rounds"))
        self.OBSERVATION_PERIOD_MS = int(self._config.get("CONSTANTS", "ob_period"))

#------------------------------------------#
# PRECONDITION:
# PARAMETERS:
#
# POSTCONDITION:
#