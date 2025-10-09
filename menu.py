from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.prompt import Prompt

console = Console()


def show_menu():
    """Display the main menu with available programs"""
    # Create a fancy table
    table = Table(
        show_header=True,
        header_style="bold magenta",
        border_style="cyan",
        title="[bold yellow]Available Programs[/bold yellow]",
        title_style="bold yellow"
    )

    table.add_column("Option", style="cyan", justify="center", width=10)
    table.add_column("Program", style="green", width=30)
    table.add_column("Description", style="white", width=40)

    # Add menu options
    table.add_row("2", "Just Playing Around", "No Program Here, Just Playing Around")
    table.add_row("1", "Weather App", "Get real-time weather for any city")
    table.add_row("0", "Exit", "Close the dashboard")

    console.print("\n")
    console.print(table)
    console.print("\n")

    return Prompt.ask(
        "[bold cyan]Select an option[/bold cyan]",
        choices=["1", "0"],
        default="1"
    )
