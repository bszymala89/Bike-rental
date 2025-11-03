class customer:
    _countID = 0

    def __init__(self, name, isRentingBike = False, isRentingHelmet = False, id = None):
        if id == None:
            customer._countID += 1
            self.id = customer._countID
        else:
            self.id = id
        self.name = name
        self.isRentingBike = isRentingBike
        self.isRentingHelmet = isRentingHelmet

    def __str__(self):
        return ", Customer Name: " + self.name + ", Customer ID: " + str(self.id)
 