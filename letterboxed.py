from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time # for sleep

options = Options()                                         # make chrome options obj.
options.add_argument("--headless")                          # make window invisible
service = Service()                                         # make chrome service obj.
driver = webdriver.Chrome(service=service, options=options) # initialize web driver

driver.get("https://www.nytimes.com/puzzles/letter-boxed")  # open letter boxed

time.sleep(5)                                               # wait for js to load

try:
    game_data = driver.execute_script("return window.gameData;")    # get game data from js
    if game_data: print("Solution:", game_data.get("ourSolution"))  # check for game data and print answer
    else: print("No gameData found.")                               # failed to find game data
except Exception as e: print("Error accessing gameData:", e)        # exception handling

driver.quit()   # close browser