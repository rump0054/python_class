tortilla = True
meat = "beef"
cheese = True
salsa = "spicy"
guacamole = False

print("Welcome to Python's Taco Stand!")

if tortilla:
    print("Great! We have a tortilla to start our taco.")
else:
    print("Oh no! We're out of tortillas. We can't make a taco!")

if meat == "chicken":
    print("Adding some delicious chicken to your taco!")
elif meat == "beef":
    print("Beef it is! Adding some juicy beef to your taco.")
elif meat == "pork":
    print("Pork fan, eh? Adding tasty pork to your taco.")
else:
    print("Looks like we're going vegetarian today!")

if cheese:
    print("Time for some cheese!")
    if salsa == "spicy":
        print("Adding extra cheese to balance out the spicy salsa!")
    else:
        print("Adding a normal amount of cheese.")
else:
    print("No cheese on this taco.")



