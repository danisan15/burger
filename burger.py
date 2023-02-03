import os

food = {
    "Stock": {
        "Regular Burger": 5,
        "Special Burger": 10,
        "Super Special Burger": 0,
        "Small Soda": 2,
        "Large Soda": 4,
    },
    "Options": {
        1: "Regular Burger",
        2: "Special Burger",
        3: "Super Special Burger",
        4: "Small Soda",
        5: "Large Soda"
    },
    "Prices": {
        "Regular Burger": 3,
        "Special Burger": 5,
        "Super Special Burger": 10,
        "Small Soda": 1,
        "Large Soda": 3,
    }
}

def val_input_num(input):
    if(input.isdigit()):
        return int(input)
    else:
        return "False"

def choose_option(option):
    choice = food["Options"][option]
    if(food["Stock"][choice] == 0):
        os.system("cls")
        print("\n<------------------Not available!-------------------->")
    else:
        order.append(choice)
        food["Stock"][choice] -= 1
        print(food["Stock"][choice])
        os.system("cls")
        print(f"\"{choice}\" succesfully added to the order")

prevStock = {}
order = []

name = input("Please, type down your name: ")
os.system("cls")
valid = 0

while(valid == 0):
    print(f"Welcome to McDonald's {name} \nPlease, type down the number to choose one of the following")
    print("1.Order \n2.Check order\n3.Check stock\n")
    option = input("Your option: ")
    os.system("cls")
    if(val_input_num(option) == "False"):
        print("\n<------------------Not a valid option!-------------------->")
        continue
    option = val_input_num(option)
    if(option <= 0 or option > 3):
        print("\n<------------------Not a valid option!-------------------->")
        continue

    valid2 = 0
    for items in food["Stock"]:
        prevStock[items] = food["Stock"][items]
    print(prevStock)

    while(valid2 == 0):
        match option:
                case 1:
                    print("Here's our menu: \n1. Regular Burger $3\n2. Special Burger $5\n3. Super Special Burger $10 \n4. Small Soda $1\n5. Large Soda $3\n\n0. Go back\n9. Proceed to checkout")
                    food_option = val_input_num(input("\nType your choice: "))
                    if(food_option == "False"):
                       os.system("cls")
                       continue
                    if(food_option == 9):
                        valid3 = 0
                        while(valid3 == 0):
                            os.system("cls")
                            print("1. Debit Card\n2.Credit Card\n0. Go back\n")
                            payment = val_input_num(input("Select payment method: "))
                            match payment:
                                case "False":
                                    os.system("cls")
                                    print("Wrong input!\n")
                                case 1:
                                    order = []
                                    os.system("cls")
                                    print("Your order is on its way!")
                                    valid3 = 1
                                    valid2 = 1
                                case 2:
                                    order = []
                                    os.system("cls")
                                    print("Your order is on its way!")
                                    valid3 = 1
                                    valid2 = 1
                                case 0:
                                    for items in prevStock:
                                        food["Stock"][items] = prevStock[items]
                                    valid3 = 1
                                    valid2 = 1
                    if(food_option < 0 or food_option > 5):
                       os.system("cls")
                       print("\n<------------------Not a valid option!-------------------->")
                    if(food_option > 0 and food_option <= 5):
                        food_option = choose_option(food_option)
                    if(food_option == 0):
                        for items in prevStock:
                             food["Stock"][items] = prevStock[items]
                        break
                case 2:
                    if(len(order) == 0):
                        os.system("cls")
                        print("<-------------Order Empty!------------->")
                        break
                    total = 0
                    os.system("cls")
                    for item in range(len(order)):
                        item_val = order[item]
                        print(f"{item_val}: ${food['Prices'][item_val]}")
                        total += food['Prices'][item_val]
                    print(f"Total is: ${total}")
                    print("<----------------------------------------->")
                    valid2 = 1
                case 3:
                    os.system("cls")
                    for item in food["Stock"]:
                        print(f"{item}: {food['Stock'][item]} units left")
                    print("<----------------------------------------->")
                    valid2 = 1
                