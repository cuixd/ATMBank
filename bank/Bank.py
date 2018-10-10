from User import User

class Bank:

    def __init__(self, bankname, atm, userlist):

        self.bankname = bankname
        self.atm = atm
        self.userlist = userlist # type:list

        admin = User("admin", "admin", None, 1)
        self.userlist.append(admin)

    #
    def login(self, user, password):

        for u in self.userlist:


            if u.username == user and u.password == password:

                return 1
            elif u.username == user and u.card.password == password:
                return 1

            continue


