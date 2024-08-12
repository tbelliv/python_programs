import pyinputplus as pyip
import sys
import time

def menu():
    menu_items = pyip.inputMenu(['Turkey ($10.00)', 'Ham and Cheese ($12.00)', 'Tuna Melt ($15.00)', 'Willowtree Chicken Salad ($15.00)', 'Build Your Own ($15.00)'], numbered=True, blank = False, timeout = 60, )
    print('You have added ', menu_items, ' to your cart. Would you like to order anything else?')
    confirmation = pyip.inputYesNo(prompt="If this is correct, press 'y' to continue. If incorrect, press 'n' to return to the menu.")
    if confirmation == 'yes' and menu_items == 'Build Your Own ($15.00)':
        byo()
    elif confirmation == 'yes':
        payment(menu_items)
    elif confirmation == 'no':
        menu()
    else:
        sys.exit()

def byo():
    bread_selection = pyip.inputMenu(['White', 'Wheat', 'Sourdough', 'Rye'], numbered=True)
    print('You chose', bread_selection)
    meat_selection = pyip.inputMenu(['Turkey', 'Ham', 'Tuna', 'Chicken', 'Willowtree'], numbered=True)
    print('You chose', meat_selection)
    cheese_selection = pyip.inputMenu(['American', 'Swiss', 'Provolone', 'Cheddar', 'None'], numbered=True)
    print('You chose', cheese_selection)
    veggies_selection = pyip.inputMenu(['Lettuce', 'Tomato', 'Onion', 'None'], numbered=True)
    print('You chose', veggies_selection)
    condiments_selection = pyip.inputMenu(['Mayo', 'Mustard', 'Ketchup', 'None'], numbered=True)
    print('You chose', condiments_selection)
    print(f'This is your order: Bread: {bread_selection} Meat: {meat_selection} Cheese: {cheese_selection} Veggies: {veggies_selection} Condiments: {condiments_selection}')
    confirmation = pyip.inputYesNo(prompt="If this is correct, press 'y' to continue. If incorrect, press 'n' to return to the menu.")
    if confirmation == 'yes':
        payment()

def payment(menu_items):
    if menu_items == 'Turkey ($10.00)':
        price=float(10.00)
    elif menu_items == 'Ham and Cheese ($12.00)':
        price=float(12.00)
    elif menu_items == 'Tuna Melt ($15.00)':
        price=float(15.00)
    elif menu_items == 'Willowtree Chicken Salad ($15.00)':
        price=float(15.00)
    elif menu_items == 'Build Your Own ($15.00)':
        price=float(15.00)
    else:
        print('Invalid menu item selected.')
        sys.exit()
    print(f'Your total is $',{price})
    payment_method = pyip.inputMenu(['Cash', 'Credit Card'], numbered=True)
    print('You chose', payment_method)
    payment = float(0.00)
    while price >= payment:
        payment = pyip.inputFloat(prompt='Enter your payment: ', min=price, max=price, blank=False, allowRegexes=['^[0-9]+\.[0-9]{2}$'], blockRegexes=['.*', 0], timeout=30)
        if payment < price:
            print('Insufficient funds. Please enter a higher amount.')
        elif payment >= price:
            print('Your change is $', payment - price)
            print('Thank you for your order! Enjoy your meal!')
            sys.exit()

if __name__ == "__main__":
    print('Hello and welcome to Spam Sandwiches. Thank you for allowing us to serve you today.')
    time.sleep(2)
    menu()