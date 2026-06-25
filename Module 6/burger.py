# Author: Erik Rumppe
# Date: 6/25/2026

# Set constants
TAX_RATE = 0.085
BURGER_PRICE = 4.99
FRIES_PRICE = 2.49
DRINK_PRICE = 1.29

def add_ingredient(ingredient):
# Adds an ingredient to the virtual burger. 
  print("Adding " + ingredient + " to your burger!")

# Example usage
add_ingredient("cheese")
add_ingredient("lettuce")
add_ingredient("bacon")

def calculate_combo_price(has_burger, has_fries, has_drink):
    # Calculates the total cost of a combo meal.
    # Assumes 8.5% tax.
    subtotal = 0
    if has_burger:
        subtotal += BURGER_PRICE
    if has_fries:
        subtotal += FRIES_PRICE
    if has_drink:
        subtotal += DRINK_PRICE

    tax = TAX_RATE * subtotal
    total_cost = subtotal + tax
    print("Total combo price: $" + "{:.2f}".format(total_cost))
    return total_cost

# Example usage
calculate_combo_price(True, True, False)

def order_decision():
    # Asks the user if they want to supersize their combo.
    supersize = input("Would you like to supersize your combo? (yes/no): ")
    if supersize.lower() == "yes":
        print("Great choice! Go big or go home!")
        return True
    else:
        print("Remember, life is short—go for the large fries!")
        return False
# Example usage
order_decision()

# Recusion example
def order_food(menu):

      # Checks if the menu list is empty       
    if not menu:
        print("Your order is complete. Enjoy your meal!")
        return
    else:   # If the menu list is not empty, prompt the user to order       
        print("Would you like to order a " + menu.pop(0) + "?") #remove an item from the list
        input()
        order_food(menu)    # The function calls itself

# Create a list of menu items and call the order_food function
menu_items = ["burger", "fries", "soda"]
order_food(menu_items)