from list import Menu
from resouces import Resource

menu = Menu()
MENU = menu.menu_list

coffee_resources = Resource()
resources = coffee_resources.resource_list

profit = 0


def resource():
    print(f'water: {resources["water"]}')
    print(f'milk: {resources["milk"]}')
    print(f'coffee: {resources["coffee"]}')
    print(f'money: {profit}')


def is_resources_enough(ordered_drink):
    """returns true if there are sufficient resources"""
    is_enough = True
    for items in ordered_drink:
        if ordered_drink[items] >= resources[items]:
            print(f'insufficient {items}')
            is_enough = False
    return is_enough


def total_coins():
    total = int(input('how many quarters?: ')) * 0.25
    total += int(input('how many dimes?: ')) * 0.10
    total += int(input('how many nickles?: ')) * 0.05
    total += int(input('how many pennies?: ')) * 0.01
    final_total = round(total, 2)
    return final_total


def transaction_successful(received_amount, cost_of_drink):
    """Returns true if the coins inserted are enough to buy the drink chosen"""
    if received_amount >= cost_of_drink:
        change = received_amount - cost_of_drink
        final_change = round(change, 2)
        print(f'here is ${final_change} in change')
        global profit
        profit += cost_of_drink
        return True
    else:
        print('Funds not received. here is your refund')
        return False


def make_coffee(drink_name, order_ingredients):
    for items in order_ingredients:
        resources[items] -= order_ingredients[items]
    print(f'here is your {drink_name}. Enjoy!')


is_on = True
while is_on:
    coffee_choice = input('What would you like? (espresso/latte/cappuccino): ').lower()
    if coffee_choice == 'off':
        is_on = False
    elif coffee_choice == 'report':
        resource()
    else:
        drink = MENU[coffee_choice]
        if is_resources_enough(drink['ingredients']):
            payment = total_coins()
            if transaction_successful(payment, drink['cost']):
                make_coffee(coffee_choice, drink['ingredients'])
