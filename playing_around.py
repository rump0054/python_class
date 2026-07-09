'''import questionary

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
).ask()'''
from rich.console import Console
from rich.panel import Panel

console = Console()


def show_fancy_banner():
    banner_text = "[bold cyan]MY TOOL[/bold cyan]\n[dim]The ultimate developer utility v1.0[/dim]"

    # Wraps the banner inside a colored box panel
    console.print(
        Panel(
            banner_text,
            expand=False,
            border_style="magenta",
            title="[yellow]Startup[/yellow]"
        )
    )


if __name__ == "__main__":
    show_fancy_banner()