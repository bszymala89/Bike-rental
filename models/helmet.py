class helmet:
    _countID = 0

    def __init__(self, brand, isAvailable = True, id = None):
        if id == None:
            helmet._countID += 1
            self.id = helmet._countID
        else:
            self.id = id

        self.isAvailable = isAvailable
        self.brand = brand

    def __str__(self):
        return "Helmet brand: " + str(self.brand)