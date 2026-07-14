# Author: Erik Rumppe
# Date: 7/14/2026

# Create a constant for cost of burger
BURGER_COST = 10.30

# Create a constant dictionary for toppings and prices
TOPPING_OPTIONS = {
    "Lettuce": .50, "Tomato": .50, "Pickle": .50, "Cheddar": 1.20, "Swiss": 1.20, "Grilled Onion": 2.40,
    "Smokehouse Bacon": 3.00, "Avocado Slices": 3.00
}

# Functions to display a greeting and a thanks message
def greeting():
    print("""
    ==================================================
                Welcome to Burgers to Go!
    ==================================================
    """)

def thanks():
    print("""
    ==================================================
               Thank You for Ordering From:
                      Burgers to Go!
    ==================================================
    """)

# Function to display toppings from list
def display_toppings(toppings):
    # Create toppings selection menu starting with 0 for Done
    print("0. Done")

    # Enumerate list and pretty print toppings
    for key, topping in enumerate(toppings, 1):
        print(f"{key}. {topping:<16} ${TOPPING_OPTIONS[topping]:.2f}")

# Function to let user select toppings
def choose_toppings():
    # Create toppings list from TOPPING_OPTIONS
    toppings_list = list(TOPPING_OPTIONS.keys())

    # Print our toppings selection screen
    display_toppings(toppings_list)

    # Create return list of selected toppings
    selected_toppings = []

    # Run while loop allowing user to choose as many toppings as they want then returning list of toppings
    while True:
        input_choice = input("Please choose a topping by selecting 0 through " + str(len(toppings_list)) + ":")
        if input_choice == "0":
            return selected_toppings
        # Validates the input - should be an int between 1 and length of options
        elif input_choice.isdecimal():
            choice_int = int(input_choice)
            if 1 <= choice_int <= len(toppings_list):
                # If input is valid, add selected choice to selected_toppings list
                selected_toppings.append(toppings_list[choice_int-1])
            continue
        else: # This might be un-needed
            break

    # Return selected_toppings
    return selected_toppings

# Function to get and validate quantity of burgers for order.  Must be between 1 and 99
def burgers_ordered():
    while True:
        ordered = input("How many burgers would you like to order (1 - 99):")
        try:
            ordered = int(ordered)
        except ValueError:
            print("Please choose a number between 1 and 99")
            continue
        if ordered < 1 or ordered > 99:
            print("Please choose a number between 1 and 99")
            continue
        break

    return ordered

# Create burger orders as dictionaries and add to list.  Return order
def create_order(orders):
    burger_orders = []

    # Create a burger by looping for each order
    for i in range(orders):
        print(f"\nPlease choose your toppings for Hamburger {i+1}")
        burger = {
            "name": f"Hamburger {i+1}",
            "toppings": choose_toppings()
        }

        # append burger to order list
        burger_orders.append(burger)

    # Return list of orders
    return burger_orders

# Print receipt for burger order
def print_receipt(burgers):
    # Prints out the receipt for the order of burgers
    total = 0
    print("\n\nRECEIPT")
    for burger in burgers:
        subtotal = BURGER_COST
        print()
        print(f"{burger["name"]:<15} ${BURGER_COST:.2f}")
        if len(burger["toppings"]) < 1:
            print(f"- {"no toppings":<16} ${0:.2f}")
        else:
            for topping in burger["toppings"]:
                print(f"- {topping:<16} ${TOPPING_OPTIONS[topping]:.2f}")
                # This was a huge pain to figure out to use () instead of {}
                subtotal += (TOPPING_OPTIONS[topping])

        total += subtotal
        print(f"{"subtotal":<15} ${subtotal:.2f}")
    print("-------------------------")
    print(f"{"TOTAL":<15} ${total:.2f}")

def main():
    # Print greeting message
    greeting()

    # Get and validate user input for how many burgers to order
    burger_quantity = burgers_ordered()

    # Create the burger order as a dictionary based on quantity ordered
    burgers = create_order(burger_quantity)

    # Print order receipt
    print_receipt(burgers)

    # Print thank you message
    thanks()

# Run main
main()