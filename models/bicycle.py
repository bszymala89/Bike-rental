class bicycle:
    _countID = 0

    def __init__(self, model, isAvailable = True, id = None):
        if id == None:
            bicycle._countID += 1
            self.id = bicycle._countID
        else:
            self.id = id
        
        self.model = model
        self.isAvailable = isAvailable

    def __str__(self):
        return "Bike Model: " + str(self.model) 