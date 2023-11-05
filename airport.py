class Airport:
    def __init__(self):
        self.airport = []

    def flight(self, key):
        if not self.inboard(key):
            self.airport.append(key)

    def nextfly(self, key):
        if self.inboard(key) and len(self.airport) > 1:
            index = self.airport.index(key)
            if index < len(self.airport) - 1:
                return self.airport[index + 1]
        return ValueError

    def inboard(self, key):
        return key in self.airport

    def showboard(self):
        return self.airport

    def removefly(self, key):
      if self.inboard(key):
        self.airport.remove(key)
      else:
        return ValueError
