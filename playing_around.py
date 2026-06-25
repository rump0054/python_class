import questionary

activity = questionary.select(
    "What would you like to do?",
    choices=["Order a pizza", "Make a reservation", "Exit"]
).ask()

print(f"You chose: {activity}")

user_data = questionary.form(
    username=questionary.text("Enter your username:"),
    password=questionary.password("Enter your password:"),
    agree=questionary.confirm("Do you accept the terms?")
).ask()

# Output is a standard dictionary:
# {"username": "...", "password": "...", "agree": True}
print(user_data)

def validate_age(text):
    if text.isdigit() and int(text) >= 18:
        return True
    return "You must be 18 or older to proceed."

age = questionary.text(
    "How old are you?",
    validate=validate_age
).ask()