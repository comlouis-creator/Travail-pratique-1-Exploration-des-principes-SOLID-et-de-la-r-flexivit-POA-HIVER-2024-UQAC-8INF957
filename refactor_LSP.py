from abc import ABC, abstractmethod

class Bird(ABC):
    @abstractmethod
    def fly(self):
        pass

class Ostrich(Bird):
    def fly(self):
        raise NotImplementedError("Ostrich cannot fly")

class Parrot(Bird):
    def fly(self):
        # Code pour faire voler le perroquet
        pass
