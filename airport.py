class Airport:
    def __init__(self):
        self.airport = []
    
    def flight(self, key):
        if not self.inboard(key):
            self.airport.append(key)

    def nextfly(self, key):
        if len(self.airport) > 1:
            return self.airport[self.airport.index(key)+1]
        else:
            return None
        
    def inboard(self, key):
        if key in self.airport:
            return True
        else:
            return False