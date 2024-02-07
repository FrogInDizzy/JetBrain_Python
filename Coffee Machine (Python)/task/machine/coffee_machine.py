def print_status(water, milk, beans, cups, money):
    print("\nThe coffee machine has:")
    print(f"{water} ml of water")
    print(f"{milk} ml of milk")
    print(f"{beans} g of coffee beans")
    print(f"{cups} disposable cups")
    print(f"${money} of money")


def buy_coffee(water, milk, beans, cups, money):
    coffee_type = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, or back to the main manu: ")
    if coffee_type == "back":  # Espresso
        return water, milk, beans, cups, money
    elif coffee_type == "1":
        if water >= 250 and beans >= 16 and cups >= 1:
            print("I have enough resources, making you a coffee!")
            return (water - 250, milk, beans - 16, cups - 1, money + 4)
        else:
            print("Sorry, not enough water, coffee beans, or cups.")
    elif coffee_type == "2":  # Latte
        if water >= 350 and milk >= 75 and beans >= 20 and cups >= 1:
            print("I have enough resources, making you a coffee!")
            return (water - 350, milk - 75, beans - 20, cups - 1, money + 7)
        else:
            print("Sorry, not enough water, milk, coffee beans, or cups.")
    elif coffee_type == "3":  # Cappuccino
        if water >= 200 and milk >= 100 and beans >= 12 and cups >= 1:
            print("I have enough resources, making you a coffee!")
            return (water - 200, milk - 100, beans - 12, cups - 1, money + 6)
        else:
            print("Sorry, not enough water, milk, coffee beans, or cups.")
    else:
        print("Invalid choice. Please choose 1, 2, or 3.")

    return water, milk, beans, cups, money  # Return unchanged values if not enough resources or invalid choice


def fill_machine(water, milk, beans, cups, money):
    added_water = int(input("Write how many ml of water you want to add: "))
    added_milk = int(input("Write how many ml of milk you want to add: "))
    added_beans = int(input("Write how many grams of coffee beans you want to add: "))
    added_cups = int(input("Write how many disposable cups you want to add: "))

    return (water + added_water,
            milk + added_milk,
            beans + added_beans,
            cups + added_cups,
            money)


def take_money(water, milk, beans, cups, money):
    print(f"I gave you ${money}")
    return water, milk, beans, cups, 0  # Setting money to 0 after taking it

def coffee_machine_action(action, water, milk, beans, cups, money):
    if action == "buy":
        return buy_coffee(water, milk, beans, cups, money)
    elif action == "fill":
        return fill_machine(water, milk, beans, cups, money)
    elif action == "take":
        return take_money(water, milk, beans, cups, money)
    elif action == "remaining":
        print_status(water, milk, beans, cups, money)
        return water, milk, beans, cups, money
    else:
        print("Invalid action. Please choose 'buy', 'fill', or 'take', remaining, exit")
        return water, milk, beans, cups, money

# Initialize the coffee machine status
water, milk, beans, cups, money = 400, 540, 120, 9, 550


while True:
    action_input = input("\nWrite action (buy, fill, take, remaining, exit): ")  # Accept user input for action
    if action_input == "exit":
        break
    water, milk, beans, cups, money = coffee_machine_action(action_input, water, milk, beans, cups, money)






