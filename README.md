# NYT Letter Boxed Scraper

This Python script uses Selenium and headless Chrome to scrape daily puzzle data from the New York Times Letter Boxed game.

## Requirements

- Python 3.7+ 
- Google Chrome
- Selenium Python package

## Setup Instructions

### 1. Install Python

Download and install Python from:
https://www.python.org/downloads/

### 2. Install Google Chrome

Download and install Google Chrome from:
https://www.google.com/chrome/

### 3. Install Selenium

#### On Mac:
```bash
pip3 install selenium
```

#### On Windows:
```bash
pip install selenium
```

## How to Run the Script

### On Mac:
```bash
python3 letterboxed.py
```

### On Windows:
```bash
python letterboxed.py
```

## Notes

- Selenium manages ChromeDriver
- The script is in headless mode, so the browser will not be visible
- 5 seconds required for the page to load before getting data
- Solution printed if found, otherwise an error message