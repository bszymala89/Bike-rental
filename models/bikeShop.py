from models.rental import rental
from models.bicycle import bicycle
import json

class bikelist:
    def __init__(self, bicycles):
        self.bicycles = bicycles

class bikeShop:
    def __init__(self, name, bikeList, helmetList, rentalDataList):
        self.name = name
        self.bikelist = bikeList
        self.helmetList = helmetList
        self.rentalDataList = rentalDataList

    def rentBike(customer, bike, date):
        rentaldata = rental(customer, bike, date)
        rentaldata.setBikeStatus(False)

    def returnBike(rentaldata):
        rentaldata.setBikeStatus(True)

    def saveBikeListStateToFile(self):
        with open("data/data.json", "w") as outfile:
            bikes = bikelist(self.bikelist)
            json.dump(bikes, outfile, indent=4, default=lambda o: o.__dict__)
            # for el in self.bikelist:
            #     json.dump(el.__dict__, outfile)

    def readBikeListStateFromFile(self):
        f = open('data/data.json',)
        data = json.load(f)
        newbikeList = []

        for i in data['bicycles']:
            newbikeList.append(bicycle(i))
        f.close()
        return newbikeList