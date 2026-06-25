tortilla = True
meat = "beef"
cheese = True
salsa = "spicy"
guacamole = True
num_of_ingredients = 0

print("Welcome to Python's Taco Stand!")

if tortilla:
    print("Great! We have a tortilla to start our taco.")
    num_of_ingredients = num_of_ingredients + 1
else:
    print("Oh no! We're out of tortillas. We'll have to make a hard shell taco!")

if meat == "chicken":
    print("Adding some delicious chicken to your taco!")
    num_of_ingredients = num_of_ingredients + 1
elif meat == "beef":
    print("Beef it is! Adding some juicy beef to your taco.")
    num_of_ingredients = num_of_ingredients + 1
elif meat == "pork":
    print("Pork fan, eh? Adding tasty pork to your taco.")
    num_of_ingredients = num_of_ingredients + 1
else:
    print("Looks like we're going vegetarian today!")

if cheese:
    print("Time for some cheese!")
    num_of_ingredients = num_of_ingredients + 1
    if salsa == "spicy":
        print("Adding extra cheese to balance out the spicy salsa!")
    else:
        print("Adding a normal amount of cheese.")
else:
    print("No cheese on this taco.")

if salsa != "":
    print("Adding " + salsa + " salsa to your taco.")
    num_of_ingredients = num_of_ingredients + 1

if guacamole:
    print("Adding guacamole!  Yum Yum!")
    num_of_ingredients = num_of_ingredients + 1
else:
    print("No guacamole on this taco.")

if num_of_ingredients >= 3:
    print("Here is your fully loaded taco!")
else:
    print("Light taco coming up!")