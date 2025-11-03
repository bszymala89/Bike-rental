from models.bicycle import bicycle
from models.bikeShop import bikeShop
from models.customer import customer
from models.helmet import helmet
from models.rental import rental

bikeRentalShop = bikeShop("bike rental",
                    [],
                    [],
                    []
                    )

# bikeRentalShop.bikelist.append(bicycle("merida"))
# bikeRentalShop.bikelist.append(bicycle("Defy Advanced 2"))
# bikeRentalShop.bikelist.append(bicycle("FastRoad AR Advanced 2"))
# bikeRentalShop.bikelist.append(bicycle("Talon 4"))

bikeRentalShop.helmetList.append(helmet("Giro"))
bikeRentalShop.helmetList.append(helmet("Bell"))
bikeRentalShop.helmetList.append(helmet("POC"))
bikeRentalShop.helmetList.append(helmet("Trek"))

def loadData():
    # data = bikeRentalShop.readBikeListStateFromFile()
    # for d in data:
    #     bikeRentalShop.bikelist.append(bicycle(d["model"], d["isAvailable"], d["id"]))
    bikeRentalShop.bikelist = bikeRentalShop.readBikeListStateFromFile()

    i = 0
    for el in bikeRentalShop.bikelist:
        i += 1
        print("[" + str(i) + "] " + str(el.__str__()))
        continue

loadData()

while True:
    print("-----")
    print("[1] Customer")
    print("[2] Employee")
    print("[3] Exit")
    option = int(input("Enter Option: "))
    if option == 1:
        print("[1] Rent Bike")
        print("[2] Return Bike")
        print("[3] Rent Helmet")
        print("[4] Return Helmet")
        print("[5] Return")
        option = int(input("Enter Option: "))
        if option == 1:
            i = 0
            for el in bikeRentalShop.bikelist:
                i += 1
                if el.isAvailable == False:
                    continue
                print("[" + str(i) + "] " + el.__str__())
            bikeOption = int(input("Enter Bike Number or 0 for exit: "))
            if bikeOption == 0:
                continue
            else:
                bike = bikeRentalShop.bikelist[bikeOption - 1]
                bike.isAvailable = False
            continue

        elif option == 2:
            continue
            customerId = int(input("Enter Customer Id: "))
        elif option == 3:
            i = 0
            for el in bikeRentalShop.helmetList:
                i += 1
                print("[" + str(i) + "] " + el.__str__())
                continue
        elif option == 4:
            pass
        elif option == 5:
            continue

    elif option == 2:
        print("[1] Save Bike List")
        print("[2] Load Bike List")
        print("[3] See Bike List")
        print("[4] Return")
        option = int(input("Enter Option: "))

        if option == 1:
            bikeRentalShop.saveBikeListStateToFile()
            continue
        elif option == 2:
            bikeRentalShop.bikelist = bikeRentalShop.readBikeListStateFromFile()
            i = 0
            for el in bikeRentalShop.bikelist:
                i += 1
                print("[" + str(i) + "] " + str(el))
                continue
        elif option == 3:
            i = 0
            for el in bikeRentalShop.bikelist:
                i += 1
                if el.isAvailable == False:
                    for e in bikeRentalShop.rentalDataList:
                        if e.bike.model == el.model:
                            print("[" + str(i) + "] " + el.__str__() + ", Available: " + str(el.isAvailable) + ", ID: " + str(el.id) + e.customer.__str__())
                            break
                else:
                    print("[" + str(i) + "] " + el.__str__() + ", Available: " + str(el.isAvailable) + ", ID: " + str(el.id))
                continue
        elif option == 4:
            continue
    elif option == 3:
        break


