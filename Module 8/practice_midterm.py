# Author: Erik Rumppe
# Date: 7/9/2026

# Create a greeting and a thanks message as constants to print easily
GREETING = """
==================================================
        Welcome to Catrinas Mexican Grill!
               Build your own taco!
==================================================
"""

THANKS = """
==================================================
           Thank You for Ordering From:
             Catrinas Mexican Grill!!
==================================================
"""

# function to display options in each list with numeric selection
def display_options(options):
    for k, v in enumerate(options, 1):
        print(f"{k}. {v}")

# Function called 'get_choice(options)' that:
def get_choice(options):
    # Display the options available with numbered choices
    display_options(options)

    # Prompts the user to enter a number and validate in while loop
    while True:
        input_choice = input("Please choose an item by entering a number between 1 and " + str(len(options)) + ": ")

        # Validates the input - should be an int between 1 length of options
        if input_choice.isdecimal():
            choice_int = int(input_choice)
            if 1 <= choice_int <= len(options):
                return options[choice_int-1]
        continue


# Create our tuples and list of ingredient/customer options
tortilla_types = ("Corn", "Flour", "Whole Wheat")
filling_types = ("Beans", "Chicken", "Fish", "Beef")
topping_options = ["Cheese", "Lettuce", "Tomatoes", "Onions", "Salsa", "Sour Cream"]

# Print out our banner greeting message
print(GREETING)

# Begin the order with the tortilla selection
print("Let's start by selecting your tortilla:")
tortilla = get_choice(tortilla_types)
print(f"{tortilla} tortilla!  Delicious!")

# Next step in the order is the filling
print("Next, please select your filling:")
filling = get_choice(filling_types)
print(f"{tortilla} tortilla filled with {filling}!  Double Delicious!!")

# Finally we do the toppings which the user can select multiple options so it is a list
# Also set a boolean for Salsa being selected to print custom message later in code
toppings = []
has_salsa = False

# Use a while true loop with prompt to add toppings using get_choices function
topping_types = topping_options.copy()
while True:
    if len(topping_types) != 0:
        print("Would you like to add some toppings to your tortilla?  Choose as many as you like.")
        choice = get_choice(['Yes', 'No'])
        if choice == 'No':
            break
        else:
            # Made selected str type because remove was complaining it was given a generic value type
            selected = str(get_choice(topping_types))

            # Check for Salsa option and flag has_salsa to True if chosen for custom print statement later
            if selected == "Salsa":
                has_salsa = True

            # Append selection to toppings and remove from topping_types list to kill loop once zero items
            toppings.append(selected)
            topping_types.remove(selected)

            continue
    else:
        # Break loop if all toppings have been selected
        print("You chose all the toppings!  Great!!")
        break

# Print out custom salsa message
if has_salsa:
    print("\nOne spicy salsa taco coming up!")

# Print out order summary.  Check if toppings were selected and print message depending on choices.
print("\nHere's your order:")
print(f"Your ordered a {tortilla} tortilla filled with {filling}!!")
if toppings:
    print("You ordered " + ", ".join(toppings) + " for toppings.")
else:
    print("Your order has no toppings.")
print("Looks delicious!  Enjoy!!!")

# Print thank you message
print(THANKS)