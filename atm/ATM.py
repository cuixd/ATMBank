import pickle
from user.User import User
from card.Card import Card

class ATM:

    userDictPath = "/Users/cuixiaodong/PycharmProjects/ATMBank/atm/userDict.txt"

    def __init__(self, bankname, userdict):

        self.bankname = bankname
        self.userdict = userdict # type:dict
        if len(userdict) == 0:
            admin = User("admin", "admin", None, 1, 1)
            self.userdict["admin"] = admin
    def indexView(self, bankname):

        viewContext = '''
            *******************************************************
            *                                                     *
            *                                                     *
            *                 欢迎使用%sATM                    *
            *                                                     *
            *                                                     *
            *                                                     *
            *******************************************************
                    '''

        print(viewContext %(bankname))

    def functionView(self, isAdmin):

        if isAdmin == 1:
            viewContext = '''
            *******************************************************
            *      开户(1)                        余额(2)           *
            *      存款(3)                        取款(4)           *
            *      转账(5)                        改密(6)           *
            *      锁定(7)                        解锁(8)           *
            *      销户(9)                        打印(0)           *
            *      退出(q)                        关机(s)           *
            *******************************************************
                        '''
        else:
            viewContext = '''
            *******************************************************
            *      开户(X)                        查询(2)           *
            *      存款(3)                        取款(4)           *
            *      转账(5)                        改密(6)           *
            *      锁定(X)                        解锁(X)           *
            *      销户(X)                        打印(0)           *
            *      退出(q)                        关机(s)           *
            *******************************************************
                        '''
        print(viewContext)

    # 查找用户
    def findUser(self, username):

        return self.userdict.get(username)

    # 登录
    def login(self, username, password):

        u = self.userdict.get(username)
        if u.password == password:

            if u.status == 1:
                return 1
            else:
                return -1
        elif u.card is not None and u.card.password == password:

            if u.status == 1:
                return 1
            else:
                return -1

        return 0

    # 开户
    def addUser(self, username, password, isAdmin):
        if isAdmin == 1:
            u = User(username, password, None, 1, 1)
        else:
            u = User(username, None, Card(abs(username.__hash__()), password, 0, 1), 0, 1)

        self.userdict[username] = u

    # 查询
    def search(self, username):

        u = self.userdict.get(username)

        if u is None:

            return -1
        else:
            if u.card is not None:
                return u.card.balance
            else:
                return 0

    # 存款
    def deposit(self, username, money):

        if money < 0:
            money = 0

        u = self.userdict.get(username)
        u.card.balance += money

    # 取款、
    def draw(self, username, money):

        if money < 0:
            money = 0

        u = self.userdict.get(username)
        u.card.balance -= money

    # 转账
    def transfer(self, username, receiver, money):
        if money < 0:
            money = 0

        self.draw(username, money)
        self.deposit(receiver,money)

    # 改密
    def changePwd(self, username, newpwd):

        u = self.userdict.get(username)

        if username == u.username and u.card is None:
            u.password = newpwd
        elif username == u.username and u.card is not None:
            u.card.password = newpwd

    # 锁定
    def lock(self, username):

        u = self.userdict.get(username)
        u.status = 0
        if  u.card is not None:
            u.card.status = 0

    # 解锁
    def unlock(self, username):

        u = self.userdict.get(username)
        u.status = 1
        u.errCount = 3
        if  u.card is not None:
            u.card.status = 1

    # 销户
    def deleteUser(self, username):

        u = self.userdict.pop(username)
        del u.card
        del u

    # 加载数据
    @classmethod
    def loadUser(self):
        with open(ATM.userDictPath, "rb") as f:
            # 将文件内容加载
            return pickle.load(f)

    # 存盘数据
    def saveUser(self):

        f = open(ATM.userDictPath, "wb")
        # 将用户字典导出
        pickle.dump(self.userdict, f)
        f.close()

    def __del__(self):

        self.saveUser()