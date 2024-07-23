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

    return True
    
def Menu():
    menu = {
        'Coffee': 3.00,
        'Espresso': 2.50,
        'Latte': 4.00,
        'Cappuccino': 4.50,
        'Tea': 2.00,
        'Herbal Tea': 2.50,
        'Hot Chocolate': 3.50,
        'Chai Latte': 3.75,
        'Iced Coffee': 3.25,
        'Iced Tea': 2.75,
        'Sandwich': 5.00,
        'Panini': 5.50,
        'Bagel': 2.00,
        'Croissant': 2.75,
        'Muffin': 2.50,
        'Scone': 3.00,
        'Cake': 4.00,
        'Cookie': 1.50,
        'Brownie': 2.25,
        'Pancakes': 5.00
    }

    print(menu)

def place_order():
    pass

def display_order():

    pass

def generate_bill():
    pass

value = False


while (True):
    print("1) Login ")
    print("2) Display Menu ")
    print("3) Place order ")
    print("4) Display order ")
    print("5) Bill  ")

    
    choice = int(input("/n select : "))

    match choice:
        case 1:
            value = login()
            if value:
                print("Login successful")
            else:
                print("Login failed")
        case 2:
            if value:
                Menu()
            else:
                print("Please login first")
        case 3:
            if value:
                place_order()
            else:
                print("Please login first")
        case 4:
            if value:
                display_order()
            else:
                print("Please login first")
        case 5:
            if value:
                generate_bill()
            else:
                print("Please login first")
        case 6:
            print("exiting the program")
            break        
        case _:
            print("Invalid choice")

    



