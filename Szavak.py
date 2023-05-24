import random

class Szavak:
    
    
    @property
    def random_szo(self):
        i = random.randint(0, len(self.adatok) - 1)
        return self.adatok[i]
    
    
    def __init__(self, sor: str) -> None:
        self.adatok = sor.split(";")
      