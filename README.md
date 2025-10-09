# CLI Dashboard

A flashy terminal dashboard with animated logos, progress bars, and multiple CLI programs.

## Features

- Cool ASCII art logo with colorful styling
- Animated progress bars on startup and transitions
- Interactive menu system
- Weather app with real-time data from OpenWeatherMap

## Installation

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Get a free API key from [OpenWeatherMap](https://openweathermap.org/api)

3. Add your API key to `weather_app.py`:
```python
API_KEY = "your_api_key_here"
```

## Usage

Run the dashboard:
```bash
python main.py
```

## Programs

### Weather App
Get real-time weather information for any city in the world with a beautiful display showing:
- Temperature
- Feels like temperature
- Humidity
- Weather conditions
- Wind speed

## Adding New Programs

To add a new program to the dashboard:

1. Create a new Python file for your program (e.g., `my_app.py`)
2. Add a function that runs your program
3. Import it in `main.py`
4. Add a menu option in `menu.py`
5. Add the program call in the main loop in `main.py`

## Requirements

- Python 3.7+
- rich
- requests
- pyfiglet
