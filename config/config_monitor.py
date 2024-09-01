CONFIG_VALID = "Valid"
CONFIG_INVALID = "Invalid"
CONFIG_EXPERIMENT_APPROVED = "Experiment approved"
CONFIG_EXPERIMENT_NOT_APPROVED = "Experiment not approved"

class ConfigMonitor:
    ### Singleton Instance
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance
    
    def __init(self):
        self._STATUS = CONFIG_VALID

    def checkConfigMinMaxRange(self, range_min, range_max):

        if (range_min > range_max) or (range_min <= 0) or (range_max <= 0): 
            return CONFIG_INVALID
        else:
            return CONFIG_VALID

# TODO: Verify that the config file is valid
    # if the vary_* = true then default_num_* = -1
        # if not, invalid
    # other invalids 
        # decimal, string for integers, etc
        # 
