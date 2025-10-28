class rental:
    def __init__(self, customer, bike, date):
        self.customer = customer
        self.bike = bike
        self.date = date
    
    def setBikeStatus(self, value):
        self.bike.isAvailable = value