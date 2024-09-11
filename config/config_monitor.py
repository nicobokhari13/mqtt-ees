
class ConfigMonitor:
    ### Singleton Instance
    _instance = None
    CONFIG_VALID = "Valid"
    CONFIG_INVALID = "Invalid"
    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance
    
    def __init__(self):

        pass 

    def validConfigMinMaxRange(self, range_min, range_max):

        if (range_min > range_max) or (range_min <= 0) or (range_max <= 0): 
            return self.CONFIG_INVALID
        return self.CONFIG_VALID

    def nonZero(self, value):
        if (value <= 0):
            return self.CONFIG_INVALID
        return self.CONFIG_VALID
