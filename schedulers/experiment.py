from abc import ABC, abstractmethod

class Experiment(ABC):
    
    @abstractmethod
    def setup(self):
        pass
    
    @abstractmethod
    def teardown(self):
        pass
    
    @abstractmethod
    def scribe_state(self):
        pass
    # TODO: See other schedulers for common methods + attributes 
    def findNextTask(self):
        pass