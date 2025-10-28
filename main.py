from models.bicycle import bicycle
from models.bikeShop import bikeShop
from models.customer import customer
from models.helmet import helmet

bikeRentalShop = bikeShop("bike rental",
                    [],
                    []
                    )

bikeRentalShop.bikelist.append(bicycle("merida"))


print("[1] Customer")
print("[2] Employee")
option = int(input("Enter Option: "))
if option == 1:
    print("[1] Rent Bike")
    print("[2] Return Bike")
    option = int(input("Enter Option: "))

    if option == 1:
        i = 0
        for el in bikeRentalShop.bikelist:
            i += 1
            print("[" + str(i) + "] " + el.__str__())
    elif option == 2:
        customerId = int(input("Enter Customer Id: "))

elif option == 2:
    print("[1] Save Bike List")
    print("[2] Load Bike List")
    print("[3] See Bike List")
    option = int(input("Enter Option: "))

    if option == 1:
        bikeRentalShop.saveBikeListStateToFile()
    elif option == 2:
        bikeRentalShop.bikelist = bikeRentalShop.readBikeListStateFromFile()
        i = 0
        for el in bikeRentalShop.bikelist:
            i += 1
            print("[" + str(i) + "] " + str(el))
    elif option == 3:
        i = 0
        for el in bikeRentalShop.bikelist:
            i += 1
            print("[" + str(i) + "] " + el.__str__() + ", Available: " + str(el.isAvailable) + ", ID: " + str(el.id))
