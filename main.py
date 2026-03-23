import art
import resource as re

def main():
    print(art.logo)
    print("Welcome to the Coffee Machine Machine!")
    machine_stock_milk = re.stock["milk"]
    machine_stock_water = re.stock["water"]
    machine_stock_coffee = re.stock["coffee"]
    machine_stock = [machine_stock_milk,machine_stock_water,machine_stock_coffee]
    money_in_machine = 0
    i = -1
    remaining_stock_in_machine = []
    remaining_stock_in_machine.append(machine_stock)
    should_continue = True
    while should_continue:
        user_choice = user_input()
        if user_choice == "report":
            print(remaining_stock_in_machine[i])
            print(f"Money Collected : ${money_in_machine}")
        elif user_choice == "off":
            print(art.m)
            should_continue = False
        elif user_choice == "cappuccino":
            money_checked = money_collection(user_choice)
            if money_checked:
                remaining_stock_in_machine.append(cappuccino(remaining_stock_in_machine,i,money_in_machine))
                money_in_machine += 40
            else:
                pass
        elif user_choice == "espresso":
            money_checked = money_collection(user_choice)
            if money_checked:
                money_in_machine += 25
                remaining_stock_in_machine.append(espresso(remaining_stock_in_machine,i))
            else:
                pass
        elif user_choice == "latte":
            money_checked = money_collection(user_choice)
            if money_checked:
                money_in_machine += 30
                remaining_stock_in_machine.append(latte(remaining_stock_in_machine,i))
            else:
                pass
        else:
            pass
        if user_choice == "cappuccino" :
            if remaining_stock_in_machine[i][0] == 0 :
                print("No Resources left Sorry")
                money_in_machine -= 40
            else:
                print(f"Here your :cappuccino:")
        elif user_choice == "latte" :
            if remaining_stock_in_machine[i][0] == 0 :
                print("No Resources left Sorry")
                money_in_machine -= 30
            else:
                print(f"Here your :latte:")
        elif user_choice == "espresso" :
            if remaining_stock_in_machine[i][0] == 0 :
                print("No Resources left Sorry")
                money_in_machine -= 25
            else:
                print(f"Here your :espresso:")
        else:
            pass


def money_collection(user_choice):
    money_inserted_5 = int(input("How much of 5 rupee are you inserting? : "))
    money_inserted_10 = int(input("How much of 10 rupee are you inserting? : "))
    money_inserted_20 = int(input("How much of 20 rupee are you inserting? : "))
    money_collected = money_inserted_5 * 5 + money_inserted_10 * 10 + money_inserted_20 * 20
    money_left = 0
    if money_collected == 0 :
        print("Not Enough money")
        money_collection()
    elif user_choice == "cappuccino":
        money_left += money_collected - 40
        print(f"Here is your Change: {money_left}")
        return True
    elif user_choice == "latte":
        money_left += money_collected - 30
        print(f"Here is your Change: {money_left}")
        return True
    elif user_choice == "espresso":
        money_left += money_collected - 25
        print(f"Here is your Change: {money_left}")
        return True
    else:
        pass


def user_input():
    user_choice = input("Press 'C' for cappuccino($40) , 'L' for latte($30), 'E' for espresso ($25): ").lower()
    if user_choice == "c":
        return "cappuccino"
    elif user_choice == "l":
        return "latte"
    elif user_choice == "e":
        return "espresso"
    elif user_choice == "report":
        return "report"
    elif user_choice == "off":
        return "off"
    else:
        print("Please enter a valid input")
        user_input()

def cappuccino(remaining_stock_in_machine,i,money_in_machine):
    c_require = re.menu["cappuccino"]["ingredients"]
    c_require_water = c_require["water"]
    c_require_milk = c_require["milk"]
    c_require_coffee = c_require["coffee"]
    left_stock_c = [0,0,0]
    if remaining_stock_in_machine[i][0] >= c_require_milk:
        left_stock_c[0]  = remaining_stock_in_machine[i][0] - c_require_milk
        left_stock_c[1]  = remaining_stock_in_machine[i][1] - c_require_water
        left_stock_c[2]  = remaining_stock_in_machine[i][2] - c_require_coffee
        return left_stock_c
    else:
        return left_stock_c



def espresso(remaining_stock_in_machine,i):
    e_require = re.menu["espresso"]["ingredients"]
    e_require_water = e_require["water"]
    e_require_coffee = e_require["coffee"]
    left_stock_e= [0, 0, 0]
    if remaining_stock_in_machine[i][1] >= e_require_water:
        left_stock_e[0] = remaining_stock_in_machine[i][0]
        left_stock_e[1] = remaining_stock_in_machine[i][1] - e_require_water
        left_stock_e[2] = remaining_stock_in_machine[i][2] - e_require_coffee
        return left_stock_e
    else:
        print("No Resources left Sorry")
        return 0

def latte(remaining_stock_in_machine,i):
    l_require = re.menu["latte"]["ingredients"]
    l_require_water = l_require["water"]
    l_require_milk = l_require["milk"]
    l_require_coffee = l_require["coffee"]
    left_stock_l = [0, 0, 0]
    if remaining_stock_in_machine[i][0] >= l_require_milk:
        left_stock_l[0] = remaining_stock_in_machine[i][0] - l_require_milk
        left_stock_l[1] = remaining_stock_in_machine[i][1] - l_require_water
        left_stock_l[2] = remaining_stock_in_machine[i][2] - l_require_coffee
        return left_stock_l
    else:
        print("No Resources left Sorry")
        return 0

main()
