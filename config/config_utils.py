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
            # holds variable: true/false

        self._vary_pubs = self._config.getboolean("VARS", "vary_pubs")
        self._vary_subs = self._config.getboolean("VARS", "vary_subs")
        self._vary_topics = self._config.getboolean("VARS", "vary_topics")

        # RANGES
            # holds minimum, maximum for variable values
        topic_range = list(map(int,self._config.get("RANGES", "topic_range").split(",")))
        sub_range = list(map(int,self._config.get("RANGES", "sub_range").split(",")))
        pub_range = list(map(int,self._config.get("RANGES", "pub_range").split(",")))
        freq_ms_range = list(map(int, self._config.get("RANGES", "freq_ms_range").split(",")))
        
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
        self.DEFAULT_PUBLISHER = int(self._config.get("DEFAULTS", "default_val_pubs"))
        self.DEFAULT_SUBSCRIBER = int(self._config.get("DEFAULTS", "default_val_subs"))
        self.DEFAULT_TOPIC = int(self._config.get("DEFAULTS", "default_val_topics")) 
        self.DEFAULT_TAIL_WINDOW_MS = int(self._config.get("DEFAULTS", "default_val_tail_window_ms"))
        self.DEFAULT_OB_PERIOD_MS = int(self._config.get("DEFAULTS", "default_val_ob_period_ms"))

        # CONSTANTS 
        self.SENSE_ENERGY = float(self._config.get("CONSTANTS", "sense_energy"))
        self.COMM_ENERGY = float(self._config.get("CONSTANTS", "comm_energy"))
        self.NUM_ROUNDS = int(self._config.get("CONSTANTS", "num_rounds"))
        self.RANDOM_LIFESPAN_CONST = int(self._config.get("CONSTANTS", "random_ob_period_ms"))
        self.MQTT_LIFESPAN_CONST = int(self._config.get("CONSTANTS", "mqtt_ob_period_ms"))
        self.EES_LIFESPAN_CONST = int(self._config.get("CONSTANTS", "ees_ob_period_ms"))
#------------------------------------------#
# PRECONDITION:
# PARAMETERS:
#
# POSTCONDITION:
#
    def instantiateConfig(self, configuration_file : str):
    
        self.saveFilePath(configuration_file)
        self.setConstants()