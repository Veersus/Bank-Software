acc = {"H":100,"He":400,"Li":600,"Be":900,"B":1100,"C":1200,"N":1400,"O":1600,"F":1900,"Ne":2000}

print(" Welcome to this atomic bank \n But you are gonna see awesome software.\n::\n show account:A,create account:B,delete account:C,")

def account_shower(k,o):# function to show account
    if m == k:
        j = int(input("password: "))
        if j == o:
            print("Transaction:T, add money:M,check balance:Q")
            b = input("Choose the program to perform: ")
            if b == "T" or b == "t":
                h = int(input("how much money do you need: "))
                total = acc[k] - h
                print(total)
            elif b =="M" or b == "m":
                H = int(input("how much money do you need: "))
                total = acc[k]+H
                print(total)
            elif b == "Q" or b == "q":
                print(acc[k])
            else:
                print("wrong program")
        else:
            print("wrong password")
    else:
        print("account not found")


for e in range(4):
    s = input("enter a program to perform: ")

    if s== "A" or s == "a":
        for u in range(2):
            m = input("enter your atomic symbol account: ")
            if m == "H":
                account_shower("H",1)
            if m == "He":
                account_shower("He",2)
            if m == "Li":
                account_shower("Li",3)
            if m == "Be":
                account_shower("Be",4)
            if m == "B":
                account_shower("B",5)
            if m == "C":
                account_shower("C",6)
            if m == "N":
                account_shower("N",7)
            if m == "O":
                account_shower("O",8)
            if m == "F":
                account_shower("F",9)
            if m == "Ne":
                account_shower("Ne",10)
            
                
       
    if s == "B" or s == "b":
        print("create a atomic account except {} this accounts".format(acc.keys))        
        g = input("enter the name of account: ")
        y = int(input("enter the cash you want to deposit: "))
        acc.insert(g,y)
        print("You use account after update")

    if s == "C" or s == "c":
        z = input("name the account you want to remove: ")
        acc.popitem(z)

      