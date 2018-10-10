from card.Card import Card

class User:

    def __init__(self, username, password, card, isAdmin, status):

        self.username = username
        self.password = password
        self.card = card
        self.isAdmin = isAdmin
        self.status = status
        self.errCount = 3  # 失败重试次数


    def __str__(self):

        return "{Username:"+self.username + ", Card:"+self.card.__str__()+ \
               ", isAdmin:"+str(self.isAdmin)+", status:"+str(self.status) +", errCount:"+str(self.errCount)+"}"

