# Author: Erik Rumppe
# Date: 7/7/2026

###
# Part 1
# Let's start with dictionaries to represent food stands
###
food_stands = {
    "Pronto Pups": "Corn Dogs",
    "Big Fat Bacon": "Bacon-on-a-Stick"
}

# Printing the food stands
print("Food stands at the fair:")
for stand, food in food_stands.items():
    print(stand + ": " + food)

# Adding a new food stand
food_stands["Fresh French Fries"] = "Fries"

# Updating a food item
food_stands["Pronto Pups"] = "Footlong Corn Dogs"

# Removing a food stand
del food_stands["Big Fat Bacon"]
print("\nAfter adding Fries stand, updating Pronto Pups and removing Big Fat Bacon:")
print(food_stands)

###
# Part 2
# Now let's use tuples for fair attractions
###
attractions = [
    ("Giant Slide", "East of the Grandstand"),
    ("Skyride", "Near Dan Patch Avenue")
]

# Printing the attractions
print("\nFair attractions:")
for attraction in attractions:
    print(attraction[0] + " is located " + attraction[1])

# Adding a new attraction
new_attraction = ("Haunted House", "Near the Midway")
attractions.append(new_attraction)
print("\nAfter adding a new attraction:")
for attraction in attractions:
    print(attraction[0] + " is located " + attraction[1])

###
# Part 3
# Finally, let's use sets for unique fair activities
###
activities = {"Riding the Giant Slide", "Watching the Parade"}

print("\nInitial set of activities:")
print(activities)

# Trying to add a duplicate activity
activities.add("Watching the Parade")
print("\nAfter trying to add a duplicate activity:")
print(activities)

# Removing an activity
activities.remove("Riding the Giant Slide")
print("\nAfter removing an activity:")
print(activities)

###
# Optional Challenge
# Let's create a daily planner using all three data structures
###
print("\n\nOPTIONAL CHALLENGE")
# First reset and create values for our food_stands(7), attractions(5), and activities(10)
food_stands = {
    "Pronto Pups": "Corn Dogs",
    "Big Fat Bacon": "Bacon-on-a-Stick",
    "Sweet Martha's": "Cookies",
    "The Cheese Curd Tacos": "Tacos With Cheese Curds",
    "Dairy Goodness Bar": "Ice Cream",
    "The Perfect Pickle": "Friend Pickles",
    "Peterson's": "Pork Chop On-a-Stick"
}

attractions = [
    ("Giant Slide", "East of the Grandstand"),
    ("Skyride", "Near Dan Patch Avenue"),
    ("Haunted House", "Near the Midway"),
    ("Butterfly House", "Before Machine Hill"),
    ("Krazy Maze", "Kids Area")
]

activities = {"Riding the Giant Slide", "Watching the Parade", "Ride the Rollercoaster", "Get a Beer", "Buy a Tractor",
              "Watch the Rodeo", "Sing Karaoke", "Take a Break", "Shop the Internation Market", "Grandstand Concert"}

daily_planner = {
    "Morning": [("Breakfast", food_stands["Sweet Martha's"]), ("Ride", attractions[0][0])],
    "Afternoon": [("Lunch", food_stands["Pronto Pups"]), ("Activity", list(activities)[0])],
    "Evening": [("Dinner", food_stands["The Cheese Curd Tacos"]), ("Ride", attractions[2][0])]
}

print("\nYour Minnesota State Fair Daily Planner:")
for time, plans in daily_planner.items():
    print(time + ":")
    for plan in plans:
        print("- " + plan[0] + ": " + plan[1])

###
# Extra Optional Challenge
# Let's create a two-day planner using all three data structures
# Re-use set variables from previous challenge - food_stands(7), attractions(5), and activities(10)
###
print("\n\nEXTRA OPTIONAL CHALLENGE")
# create list of activities so you don't duplicate an activity
activities_list = list(activities)

days = [
    {
        "Morning": [
            ("Breakfast", food_stands["Sweet Martha's"]),
            ("Ride", attractions[0][0]),
            ("Ride", attractions[1][0]),
            ("Activity", activities_list[0])
        ],
        "Afternoon": [
            ("Lunch", food_stands["Pronto Pups"]),
            ("Snack", food_stands["Big Fat Bacon"]),
            ("Activity", activities_list[1]),
            ("Activity", activities_list[2])
        ],
        "Evening": [
            ("Dinner", food_stands["The Cheese Curd Tacos"]),
            ("Ride", attractions[2][0]),
            ("Activity", activities_list[7])
        ]
    },
    {
        "Morning": [
            ("Breakfast", food_stands["The Perfect Pickle"]),
            ("Ride", attractions[3][0]),
            ("Activity", activities_list[3])
        ],
        "Afternoon": [
            ("Lunch", food_stands["Dairy Goodness Bar"]),
            ("Activity", activities_list[4]),
            ("Activity", activities_list[6])
        ],
        "Evening": [
            ("Dinner", food_stands["Peterson's"]),
            ("Ride", attractions[4][0]),
            ("Activity", activities_list[8]),
            ("Activity", activities_list[9])
        ]
    },
]

print("\nYour Two Day Minnesota State Fair Daily Planner:")
counter = 1
for day in days:
    print("\nDay " + str(counter) + ":")
    for time, plans in day.items():
        print(time + ":")
        for plan in plans:
            print("- " + plan[0] + ": " + plan[1])
    counter += 1