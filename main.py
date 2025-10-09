#!/usr/bin/env python3
"""
CLI Dashboard - A flashy terminal dashboard with multiple programs
"""

import sys
from rich.console import Console
from utils import show_logo, fake_progress_bar, clear_screen
from menu import show_menu
from weather_app import run_weather_app

console = Console()


def startup_animation():
    """Show the startup animation with logo and progress bar"""
    clear_screen()
    show_logo()
    fake_progress_bar("Initializing CLI Dashboard", duration=2)


def main():
    """Main application loop"""
    # Show startup animation
    startup_animation()

    while True:
        clear_screen()
        show_logo()

        # Show menu and get user choice
        choice = show_menu()

        if choice == "1":
            # Run weather app
            clear_screen()
            fake_progress_bar("Loading Weather App", duration=1)
            clear_screen()
            run_weather_app()

        elif choice == "0":
            # Exit
            clear_screen()
            console.print("\n[bold cyan]👋 Thanks for using CLI Dashboard![/bold cyan]\n")
            fake_progress_bar("Shutting down", duration=1)
            console.print("\n[bold green]✨ Goodbye![/bold green]\n")
            sys.exit(0)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        clear_screen()
        console.print("\n\n[bold yellow]⚠️  Interrupted by user[/bold yellow]")
        console.print("[bold cyan]👋 Goodbye![/bold cyan]\n")
        sys.exit(0)
