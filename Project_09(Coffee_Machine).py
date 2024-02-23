from Coffee_data import coffee
import Qrcode
profit = 0
resources = {
    "water" : 700,
    "milk": 1500,
    "coffee" : 500,
    "foam": 200,
    "chocolate":500
}

def check_resources(ingredients):
    for item in ingredients:
        if ingredients[item]>resources[item]:
            print(f"Sorry there are not enough {item}")
            return False
        return True
    
def payments(c_type):
    filename = "payment_qr_code.png"
    choose = input("Select mode of payment (Online/ offline) : ")
    if choose == 'Online':
       Qrcode
       for item in c_type:
           total = c_type['cost'] 
           Qrcode.display_qr_code(filename)
       return total
    else :
       coin_five = int(input("How many 5rs coin? : "))
       coin_ten = int(input("How many 10rs coin? : "))
       coin_twenty = int(input("How many 20rs coin? : "))
       total = coin_five*5+coin_ten*10+coin_twenty*20
       return total
def success(money_recieved, coffee_cost):
    global profit
    if money_recieved>= coffee_cost:
        profit += coffee_cost
        money_left = money_recieved-coffee_cost
        print(f"Here is Rs{money_left} in change.")
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False
def make_coffee(choice, c_ingredients):
    for item in c_ingredients:
        resources[item] -= c_ingredients[item]
    print(f"Here is your {choice} ☕ ... Enjoy!!")
is_on = True
while is_on:
    choice = input("What would you like to have?(Espresso/Americano/Latte/Cappuccino): ")
    if choice == 'off':
        is_on = False
    elif choice == 'report':
        print(f"""Water = {resources['water']}ml\nMilk = {resources['milk']}ml
Coffee = {resources['coffee']}ml\nFoam = {resources['foam']}ml\nChocolate = {resources['chocolate']}ml""")
        print(f"Money = Rs{profit}")
    else:
        coffee_type = coffee[choice]
        print(coffee_type)
        if check_resources(coffee_type['ingredients']):
            payment = payments(coffee_type)
            if success(payment, coffee_type['cost']):
                make_coffee(choice, coffee_type['ingredients'])