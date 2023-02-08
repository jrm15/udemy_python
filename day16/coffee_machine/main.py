from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


menu = Menu()
maker = CoffeeMaker()
money = MoneyMachine()


while True:
    selection = str(input('What would you like?' + menu.get_items()))
    if selection == 'report':
        print(maker.report())
        print(money.report())
    else:
        user_selection = menu.find_drink(selection)
        sufficient = maker.is_resource_sufficient(user_selection)
        if sufficient:
            money.make_payment(user_selection.cost)
            maker.make_coffee(user_selection)