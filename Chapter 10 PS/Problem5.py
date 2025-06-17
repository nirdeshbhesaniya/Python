from random import randint

class Train:
    
    def __init__(self, trainNo):
        self.trainNo = trainNo
        
    def book(self, fro, to):
        self.fro = fro
        self.to = to
        self.pnr = randint(1000000000, 9999999999)
        print(f"Ticket booked from {self.fro} to {self.to} with PNR: {self.pnr}")

    def getStatus(self, fro, to):
        print(f"Train No: {self.trainNo}, From: {self.fro}, To: {self.to}, PNR: {self.pnr} is Runnig on time")

    def getFare(self, fro, to):
        print(f"Ticket fare in train no: {self.trainNo} from {self.fro} to {self.to} is Rs. 500")
            
t = Train(12399)
t.book("Rampur", "Delhi")
t.getStatus("Rampur", "Delhi")
t.getFare("Rampur", "Delhi")
# The methods getStatus and getFare are defined inside the book method, which is not correct.
# They should be defined at the class level, not inside another method.