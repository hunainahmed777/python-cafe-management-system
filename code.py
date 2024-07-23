def login():
    while (True):

        Username = input("please enter ther user name : ")
    

        if Username == "hunainahmed":
            break

        else:
            print("you have entered incorrect Username")
    while (True):

        password = input("please enter the password : ")
        if password == "okay":
            break

        else:
            print("you have entered incorrect password : ")
    









print("1) login ")
print("2) Menue and place order ")
print("3) Bill  ")


choice = int(input("/n select : "))

if choice == 1:
    login()