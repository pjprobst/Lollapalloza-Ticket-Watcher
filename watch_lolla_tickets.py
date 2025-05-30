import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests

PUSHOVER_USER_KEY = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
PUSHOVER_API_TOKEN = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'

def send_pushover(message):
    data = {
        "token": PUSHOVER_API_TOKEN,
        "user": PUSHOVER_USER_KEY,
        "message": message
    }
    response = requests.post("https://api.pushover.net/1/messages.json", data=data)
    if response.status_code == 200:
        print("Pushover alert sent.")
    else:
        print("X Pushover failed:", response.text)

def get_lowest_ticket_price(previous_lowest):
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")

    driver = webdriver.Chrome(options=options)
    driver.get("https://www.ticketexchangebyticketmaster.com/grant-park-chicago/lollapalooza-tickets-chicago-il/tickets/4542048")

    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.TAG_NAME, "body"))
    )

    soup = BeautifulSoup(driver.page_source, 'html.parser')
    driver.quit()

    lines = soup.get_text(separator="\n").splitlines()
    lines = [line.strip() for line in lines if line.strip()]

    prices = []

    for i in range(len(lines) - 1):
        current_line = lines[i]
        next_line = lines[i + 1]

        if current_line.startswith('$') and next_line.startswith('('):
            try:
                price = float(current_line.replace('$', '').replace(',', ''))
                prices.append(price)
            except ValueError:
                continue

    if prices:
        lowest = min(prices)
        print(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] Lowest ticket price: ${lowest:.2f}")
        if previous_lowest is None:
            return lowest
        elif lowest != previous_lowest:
            print("PRICE CHANGE!!!!!")
            send_pushover(f"🎟️ Lollapalooza ticket price changed: ${previous_lowest:.2f} → ${lowest:.2f}")
            return lowest
        else:
            return previous_lowest
    else:
        print(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] No ticket prices found.")
        return previous_lowest
    
if __name__ == "__main__":
    lowest = None
    while True:
        try:
            lowest = get_lowest_ticket_price(lowest)
        except Exception as e:
            print(f"Error: {e}")
        time.sleep(15)
