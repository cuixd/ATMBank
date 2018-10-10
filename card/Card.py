

class Card:

    def __init__(self, id, password, balance, status):

        self.id = id
        self.password = password
        self.balance = balance
        self.status = status


    def __str__(self):

        return "{id:"+str(self.id) + ", password:"+str(self.password)+", balance:"+str(self.balance) + ", status:"+str(self.status)+"}"