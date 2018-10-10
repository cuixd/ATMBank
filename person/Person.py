import os.path
import sys
from user.User import User
from card.Card import Card
from atm.ATM import ATM


if __name__ == "__main__":

    userDict = {}

    if os.path.exists(ATM.userDictPath) and os.path.getsize(ATM.userDictPath):
        userDict = ATM.loadUser()

    bank = ATM("逗逼银行", userDict)
    loopflag = True
    while loopflag:

        bank.indexView(bank.bankname)
        inputUser = input("请输入用户名：")
        crrUser = bank.userdict.get(inputUser)
        if  crrUser is None:

            print("输入的用户不存在，请重新输入")
            continue
        inputPwd = input("请输入密码：")
        res = bank.login(inputUser, inputPwd)
        if res == 1:

            print("登陆成功，即将进入主功能界面")

            # 登录成功，重置重试次数
            crrUser.errCount = 3
            isAdmin = bank.userdict.get(inputUser).isAdmin

            while True:

                bank.functionView(isAdmin)
                inputFunc = input("请选择功能：")

                if inputFunc == "1":

                    newUser = input("请输入开户名：")
                    isAdm = input("是否管理员(0否 1是)：")
                    newPwd = ""
                    if isAdm == "1":
                        newPwd = input("请输入新管理员密码：")
                    elif isAdm == "0":
                        newPwd = input("请输入卡密码：")
                    bank.addUser(newUser, newPwd, int(isAdm))

                    for u in bank.userdict.keys():
                        print(bank.userdict[u])

                elif inputFunc == "2":

                    print("当前余额：%d" %(bank.search(inputUser)))

                elif inputFunc == "3":

                    inputMoney = int(input("请输入存款金额："))
                    bank.deposit(inputUser, inputMoney)
                    print("成功存入"+str(inputMoney))
                elif inputFunc == "4":

                    inputMoney = int(input("请输入取款金额："))
                    bank.draw(inputUser, inputMoney)
                    print("成功取出" + str(inputMoney))
                elif inputFunc == "5":

                    inputReceiver = input("请输入转账对方用户名：")
                    if bank.userdict.get(inputReceiver) is None:
                        print("对不起，转入账户不存在，退出本次操作")
                        continue
                    elif bank.userdict.get(inputReceiver).status == 0:
                        print("对不起，转入账户已被锁定，无法转账")
                        continue
                    inputMoney = int(input("请输入转账金额："))
                    bank.transfer(inputUser, inputReceiver, inputMoney)
                    print("成功转账" + str(inputMoney) + "到" + inputReceiver)

                elif inputFunc == "6":
                    inputnewPwd = input("请输入新密码：")
                    inputnewPwdr = input("请再次新密码：")

                    if inputnewPwd == inputnewPwdr:
                        bank.changePwd(inputUser, inputnewPwd)
                        print("密码修改成功")
                    else:
                        print("两次输入不匹配，退出本次操作")
                        continue
                elif inputFunc == "7":
                    inputLockUser = input("请输入要锁定的账户名：")
                    if bank.userdict.get(inputLockUser) is None:
                        print("对不起，目标账户不存在，退出本次操作")
                        continue
                    bank.lock(inputLockUser)
                    print(inputLockUser+"已被成功锁定")

                elif inputFunc == "8":
                    inputunLockUser = input("请输入要解锁的账户名：")
                    if bank.userdict.get(inputunLockUser) is None:
                        print("对不起，目标账户不存在，退出本次操作")
                        continue
                    bank.unlock(inputunLockUser)
                    print(inputunLockUser+"已成功解锁")

                elif inputFunc == "9":
                    inputDropUser = input("请输入要销户的账户名：")
                    if bank.userdict.get(inputDropUser) is None:
                        print("对不起，目标账户不存在，退出本次操作")
                        continue
                    bank.deleteUser(inputDropUser)
                    print(inputDropUser + "已成功销户")

                elif inputFunc == "0":

                    if isAdmin == 1:
                        print("当前银行中的全部账户：")
                        for u in bank.userdict.keys():
                            print(bank.userdict[u])
                    else:
                        print("您的账户信息：")
                        print(crrUser)

                elif inputFunc == "q":
                    break
                elif inputFunc == "s":
                    loopflag = False
                    break

        elif res == -1:
            print("该账户已被锁定，请联系管理员")
        else:

            crrUser.errCount -= 1
            print("密码输入错误，您还有" + str(crrUser.errCount)+"次重试机会")
            if crrUser.errCount == 0:
                bank.lock(inputUser)
                print("您的账户被锁定，请联系管理员解锁")
            continue