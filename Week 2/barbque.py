# Author: Erik Rumppe
# Date: 6/25/2026

# Used PyInputPlus 0.2.12 module to make things more fun and interactive
# pip install pyinputplus
import pyinputplus as pyip

# Set constants first
SANDWICH_PRICE = 8
PLATTER_PRICE = 12

# Get customer name, automatic error handling for empty strings
customer_name = pyip.inputStr('Please enter your name: ')

# Get customer meal choice with automatic error handling for incorrect input then set meal_price based on choice.
# lower() method called although technically not necessary
meal_choice = pyip.inputMenu(['Sandwich', 'Platter'], prompt="Do you want a Sandwich or Platter meal? \n")
if meal_choice.lower() == "sandwich":
    meal_price = SANDWICH_PRICE
elif meal_choice.lower() == "platter":
    meal_price = PLATTER_PRICE

# Get customer meal count greater than 0 with automatic error handling for non integer numbers then calculate toal_cost of meals
num_meals = pyip.inputInt(prompt="How many meals do you want? ", greaterThan=0)
total_cost = meal_price * num_meals

# Get customer choice on extra sauce with with automatic error handling for incorrect input then recalculate total_cost
# based on customer selection
extra_sauce = pyip.inputChoice(['yes', 'no'], prompt='Do you want extra sauce? (yes/no): ')
if extra_sauce.lower() == "yes":
    total_cost += 0.5 * num_meals

# Calculate the original total without extra sauce and set boolean for sauce_added
original_total = meal_price * num_meals
sauce_added = extra_sauce == "yes"

# Print an order summary of customers entire order formatting costs to dollars and cents.
print("\nOrder Summary:")
print("Customer Name: " + customer_name)
print("Meal Type: " + meal_choice + " meal")
print("Number of Meals: " + str(num_meals))
print("Extra Sauce: " + ("Yes" if sauce_added else "No"))
print("Original Total: $" + "{:.2f}".format(original_total))
print("Final Total: $" + "{:.2f}".format(total_cost))