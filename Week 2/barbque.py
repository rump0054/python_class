customer_name = input("Please enter your name:")
sandwich_price = 8
platter_price = 12

meal_choice = input("Do you want a sandwich meal or platter meal? (sandwich/platter): ")
if meal_choice.lower() == "sandwich":
    meal_price = sandwich_price
elif meal_choice.lower() == "platter":
    meal_price = platter_price
else:
    print("Naughty user!  Defaulting to sandwich.")
    meal_choice = "sandwich"
    meal_price = sandwich_price

