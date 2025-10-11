import os
import requests
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.prompt import Prompt
from rich.text import Text
from utils import fake_progress_bar
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

console = Console()

# You'll need to get your own API key from https://openweathermap.org/api
API_KEY = os.getenv("OPENWEATHER_API_KEY")
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"


def get_weather_emoji(description):
    """Return weather emoji based on description"""
    description = description.lower()
    if "clear" in description:
        return "☀️"
    elif "cloud" in description:
        return "☁️"
    elif "rain" in description:
        return "🌧️"
    elif "thunder" in description:
        return "⛈️"
    elif "snow" in description:
        return "❄️"
    elif "mist" in description or "fog" in description:
        return "🌫️"
    else:
        return "🌤️"


def display_weather(weather_data):
    """Display weather information in a flashy way"""
    # Extract data
    city = weather_data["name"]
    country = weather_data["sys"]["country"]
    temp = weather_data["main"]["temp"]
    feels_like = weather_data["main"]["feels_like"]
    humidity = weather_data["main"]["humidity"]
    description = weather_data["weather"][0]["description"].title()
    wind_speed = weather_data["wind"]["speed"]

    emoji = get_weather_emoji(description)

    # Create title
    title = Text(f"{emoji}  Weather for {city}, {country}  {emoji}", style="bold yellow")

    # Create weather info table
    table = Table(show_header=False, border_style="cyan", padding=(0, 2))
    table.add_column("Property", style="bold magenta", width=20)
    table.add_column("Value", style="bold white", width=30)

    table.add_row("🌡️  Temperature", f"{temp}°F") 
    table.add_row("🤔 Feels Like", f"{feels_like}°F")
    table.add_row("💧 Humidity", f"{humidity}%")
    table.add_row("🌤️  Conditions", description)
    table.add_row("💨 Wind Speed", f"{wind_speed} m/s")

    # Create panel
    panel = Panel(
        table,
        title=title,
        border_style="bright_cyan",
        padding=(1, 2)
    )

    console.print("\n")
    console.print(panel)
    console.print("\n")


def run_weather_app():
    """Main function to run the weather app"""
    console.print("\n[bold cyan]═══ Weather App ═══[/bold cyan]\n")

    city = Prompt.ask("[bold green]Enter city name[/bold green]")

    fake_progress_bar("Fetching weather data", duration=1.5)

    try:
        # Make API request
        params = {
            "q": city,
            "appid": API_KEY,
            "units": "imperial"  # Use "metric" for Celsius
        }

        response = requests.get(BASE_URL, params=params)

        if response.status_code == 200:
            weather_data = response.json()
            display_weather(weather_data)
        elif response.status_code == 404:
            console.print(f"\n[bold red]❌ City '{city}' not found. Please try again.[/bold red]\n")
        elif response.status_code == 401:
            console.print("\n[bold red]❌ Invalid API key or API key not activated yet.[/bold red]\n")
            console.print("[yellow]Note: New API keys can take up to 2 hours to activate.[/yellow]")
            console.print(f"[yellow]API Response: {response.text}[/yellow]\n")
        else:
            console.print(f"\n[bold red]❌ Error: {response.status_code}[/bold red]\n")
            console.print(f"[yellow]Response: {response.text}[/yellow]\n")

    except requests.exceptions.RequestException as e:
        console.print(f"\n[bold red]❌ Network error: {str(e)}[/bold red]\n")

    # Wait for user to continue
    Prompt.ask("\n[dim]Press Enter to return to menu[/dim]", default="")
