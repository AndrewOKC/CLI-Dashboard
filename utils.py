import time
from rich.console import Console
from rich.progress import Progress, SpinnerColumn, BarColumn, TextColumn
from rich.panel import Panel
from rich.text import Text
from pyfiglet import figlet_format

console = Console()


def show_logo():
    """Display a cool ASCII art logo with gradient colors"""
    logo = figlet_format("CLI DASHBOARD", font="slant")

    # Create gradient text
    text = Text(logo)
    text.stylize("bold cyan")

    panel = Panel(
        text,
        border_style="bright_magenta",
        padding=(1, 2)
    )

    console.print(panel)


def fake_progress_bar(description="Loading", duration=2):
    """Create a fake progress bar animation"""
    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        BarColumn(complete_style="cyan", finished_style="bright_cyan"),
        TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),
        console=console
    ) as progress:
        task = progress.add_task(f"[cyan]{description}...", total=100)

        # Simulate progress with varying speeds
        chunks = [10, 15, 20, 25, 15, 10, 5]
        for chunk in chunks:
            time.sleep(duration / len(chunks))
            progress.update(task, advance=chunk)


def clear_screen():
    """Clear the console screen"""
    console.clear()
