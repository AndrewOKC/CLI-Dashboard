# CLI Dashboard

A flashy terminal dashboard with animated logos, progress bars, and multiple CLI programs.

![Dashboard Home](images/Daahboard_Home.png)

## Features

-   Cool ASCII art logo with colorful styling
-   Animated progress bars on startup and transitions
-   Interactive menu system
-   Weather app with real-time data from OpenWeatherMap (in Fahrenheit)
-   AI Chatbot powered by Gemini

## Installation

1. Install dependencies:

```bash
pip install -r requirements.txt
```

2. Create a `.env` file in the project root (you can copy `.env.example`):

```bash
cp .env.example .env
```

3. Add your API keys to the `.env` file:
    - Get a free API key from [OpenWeatherMap](https://openweathermap.org/api)
    - Get an API key from [Google AI Studio](https://makersuite.google.com/app/apikey) for the AI Chatbot

```
OPENWEATHERMAP_API_KEY=your_openweathermap_key_here
GEMINI_API_KEY=your_gemini_key_here
```

## Usage

Run the dashboard:

```bash
python3 main.py
```

> **Note for Mac users:** Use `python3` and `pip3` commands. If you have Python 3 set as your default, you can use `python` and `pip` instead.

## Programs

### Weather App

Get real-time weather information for any city in the world with a beautiful display showing:

-   Temperature (Fahrenheit)
-   Feels like temperature (Fahrenheit)
-   Humidity
-   Weather conditions
-   Wind speed

![Weather App](images/Dashboard_Weather_App_New.png)

### AI Chatbot

Interactive AI assistant powered by Gemini that can:

-   Answer questions
-   Help with problem-solving
-   Have natural conversations
-   Provide information on various topics

![AI Chatbot](images/Dashboard_AI_Chat_App.png)

## Adding New Programs

To add a new program to the dashboard:

1. Create a new Python file for your program (e.g., `my_app.py`)
2. Add a function that runs your program
3. Import it in `main.py`
4. Add a menu option in `menu.py`
5. Add the program call in the main loop in `main.py`

## Requirements

-   Python 3.7+
-   rich==13.7.0
-   requests==2.31.0
-   pyfiglet==1.0.2
-   python-dotenv==1.0.0
-   google-generativeai>=0.8.0
