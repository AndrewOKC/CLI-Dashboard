import os
import google.generativeai as genai
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from rich.markdown import Markdown
from rich.text import Text
from utils import fake_progress_bar
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

console = Console()

# Get API key from environment
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")


def initialize_gemini():
    """Initialize the Gemini API with the API key"""
    if not GEMINI_API_KEY:
        console.print("\n[bold red]❌ GEMINI_API_KEY not found in .env file[/bold red]\n")
        console.print("[yellow]Please add your Gemini API key to the .env file:[/yellow]")
        console.print("[yellow]GEMINI_API_KEY=your_api_key_here[/yellow]\n")
        console.print("[dim]Get your free API key at: https://makersuite.google.com/app/apikey[/dim]\n")
        return None

    try:
        # Configure to use REST API instead of gRPC to avoid network issues
        genai.configure(api_key=GEMINI_API_KEY, transport='rest')
        # Use the latest flash model (fast and free)
        model = genai.GenerativeModel('gemini-2.5-flash')
        return model
    except Exception as e:
        console.print(f"\n[bold red]❌ Error initializing Gemini: {str(e)}[/bold red]\n")
        return None


def display_message(role, message):
    """Display a chat message with styling"""
    if role == "user":
        title = Text("🧑 You", style="bold cyan")
        border_style = "cyan"
        content_style = "white"
    else:
        title = Text("🤖 Gemini AI", style="bold magenta")
        border_style = "magenta"
        content_style = "white"

    # Use Markdown for AI responses to support formatting
    if role == "assistant":
        content = Markdown(message)
    else:
        content = Text(message, style=content_style)

    panel = Panel(
        content,
        title=title,
        border_style=border_style,
        padding=(1, 2)
    )

    console.print(panel)


def run_chatbot_app():
    """Main function to run the AI chatbot app"""
    console.print("\n[bold cyan]═══ AI Chatbot (Powered by Gemini) ═══[/bold cyan]\n")

    fake_progress_bar("Initializing AI", duration=1)

    model = initialize_gemini()
    if not model:
        Prompt.ask("\n[dim]Press Enter to return to menu[/dim]", default="")
        return

    # Start a chat session
    chat = model.start_chat(history=[])

    console.print("\n[bold green]✨ AI Chatbot ready! Type your messages below.[/bold green]")
    console.print("[dim]Type 'exit', 'quit', or 'back' to return to the menu.[/dim]\n")

    while True:
        # Get user input
        user_message = Prompt.ask("\n[bold cyan]You[/bold cyan]")

        # Check for exit commands
        if user_message.lower() in ['exit', 'quit', 'back', 'q', '/exit', '/quit', '/back']:
            console.print("\n[bold yellow]👋 Ending chat session...[/bold yellow]\n")
            break

        if not user_message.strip():
            console.print("[yellow]Please enter a message.[/yellow]")
            continue

        # Display user message
        console.print()
        display_message("user", user_message)

        # Show thinking animation
        fake_progress_bar("AI is thinking", duration=10)

        try:
            # Send message to Gemini
            response = chat.send_message(user_message)

            # Display AI response
            console.print()
            display_message("assistant", response.text)

        except Exception as e:
            console.print(f"\n[bold red]❌ Error: {str(e)}[/bold red]\n")
            console.print("[yellow]There was an error communicating with the AI.[/yellow]")
            console.print("[yellow]Please check your API key and internet connection.[/yellow]\n")

    # Return to menu
    console.print()
