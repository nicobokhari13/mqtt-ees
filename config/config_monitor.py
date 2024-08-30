class ConfigMonitor:
    ### Singleton Instance
    _instance = None
    
    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance
    
    def __init(self):
        pass

# TODO : print config status at the beginng of each experiment round

# TODO: Verify that the config file is valid
    # if the vary_* = true then default_num_* = -1
        # if not, invalid
    # other invalids 
        # decimal, string for integers, etc
        # 
