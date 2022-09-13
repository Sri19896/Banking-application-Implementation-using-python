
from pickle import NONE
import time
import pandas as pd


class IB:
    def __init__(y,  Username, Password):
        y.name = Username
        y.Password = Password

    def printuserinfo(x):
        print('welcome ,you sucessfully  Signed in  with ', x.name)


class withdraw(IB):
    def __init__(y,  Username, Password):
        super().__init__(Username, Password)

    def printamount(z):
        av = A[I]
        money = input('please enetr how mcuh money you want to withdraw  ')

        money = money.lstrip()
        money = money.rstrip()
        money = int(money)
        if money <= av:
            df.loc[[I], 'Money with draw'] = money
            fb = int(A[I] - money)
            df.loc[[I], 'Final Balance'] = fb
            df.to_csv('UDB.csv', index=False)
            print('Processing your Request......')
            time.sleep(1.5)
            print('Transaction sucessfull ,Please take your card')
            time.sleep(1)
            print('Avilaible Balance in your account is ', fb)
            time.sleep(1.5)
            print('Please collect your cash')
        if money >= av:
            print('Insufficent balance')


class deposit(IB):
    def __init__(y,  Username, Password):
        super().__init__(Username, Password)

    def wd(w):
        cash = input('Please Enter how much Money yout deposit  ')
        time.sleep(1.5)
        print('please wait  processsing request ')
        m = input('Please insert your cash')
        time.sleep(1)
        print('Please wait counting money')
        time.sleep(1.5)
        d = input(cash+'e  you want to  deposit YES /NO   ')
        if d == 'YES':
            print('please wait processing request')
            time.sleep(1.5)
            print('money  deposit sucessful')
            s = df.loc[[I], 'Final Balance']
            df.loc[[I], 'Money deposited'] = cash
            fb = int(A[I]) + int(cash)
            df.loc[[I], 'Final Balance'] = fb
            print('Avilaible Balance in your account is ', fb)
            df.to_csv('UDB.csv', index=False)

        if d == 'NO':
            f = input('do you want cancel the transaction ??  ')
            if f == 'YES':
                print('traanction cancelled please  take your  card')
                if f == 'NO':
                    print('Please collect your cash')


class PINCHANGE(IB):
    def __init__(y,  Username, Password):
        super().__init__(Username, Password)

    def pc(c):
        time.sleep(1)
        while True:
            np = input('please Enter your new password  ')
            np = np.lstrip()
            np = np.rstrip()
            time.sleep(1)
            if len(np) > 1:
                np = int(np)
                print('Please wait checking ')
                if np == P[I]:
                    print('New password is same as pervious  password')
                    continue
                else:
                    print('Password chnged sucessfully')
                    df.loc[[I], 'NEWPIN'] = np
                    df.to_csv('UDB.csv', index=False)
                    break
            else:
                print('Please enter valid Password')
                print(
                    'Password must be  8 charecters and have 2 numbers , 2 special charecters ')
            continue


class showmoney(IB):
    def __init__(y,  Username, Password):
        super().__init__(Username, Password)

    def printbalance(g):
        print('Please Wait Processing')
        time.sleep(1.5)
        print('Aviable balance in your Acoount is', B[I])


while True:
    df = pd.read_csv('UDB.csv')
    U = df['User']
    P = df['PIN']
    P = list(P)
    A = df['Current Balance']
    B = df['Final Balance']
    B = list(B)
    A = list(A)
    U = list(U)
    I = NONE
    f = input('Enter your username ')
    f = f.rstrip()
    f = f.lstrip()
    if f in U:
        p = input('Eter your ATM PIN  ')
        I = U.index(f)
        p = int(p)
        if p == P[I]:
            print('Login Sucess')
            break
        else:
            print('Wrong Pin Try again')
        continue
        break
    else:
        print('wrong username')
    continue
s = IB(f, p)
s.printuserinfo()
time.sleep(1)
while True:
    print('Please choose  option from  the list')
    print('1.Money  with draw')
    print('2.Money Deposit')
    print('3.ATM PIN CHANGE')
    print('4.Balance Enquiry')
    print('5.Exit')
    ac = input('please enetr your option here ')
    ac = ac.lstrip()
    ac = ac.rstrip()
    ac = int(ac)
    if ac == 1:
        w = withdraw(f, p)
        w.printamount()
    if ac == 2:
        d = deposit(f, p)
        d.wd()
    if ac == 3:
        c = PINCHANGE(f, p)
        c.pc()
    if ac == 4:
        blc = showmoney(f, p)
        blc.printbalance()
    time.sleep(1.5)
    if ac == 5:
        E = input('Do you  want to exit ??   ')
        if E == 'YES':
            break
        if E == 'NO':
            continue
    continue
