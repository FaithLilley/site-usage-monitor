import re
import datetime
import csv
import random
import time
from playwright.sync_api import sync_playwright

# URL of the website to scrape
URL = "https://www.dndbeyond.com/forums"

def fetch_data():
    with sync_playwright() as p:
        # Need to set headless as false, so as to not trip Perimeter X
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.set_extra_http_headers({
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
            "Accept-Language": "en-US,en;q=0.9",
        })
        page.goto(URL)
        page.wait_for_timeout(5000)  # Wait for JavaScript to load

        # Get the page content
        page_content = page.content()

        # Create filename with timestamp
        timestamp = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
        file_name = f"pages/forums_{timestamp}.html"

        # Save the content to a file
        with open(file_name, "w", encoding="utf-8") as file:
            file.write(page_content)

        try:
            # Get the rendered page source
            html_content = page.content()

            # Define a regex pattern to extract the numbers
            pattern = r"Online Users: (\d{1,3}(?:,\d{3})*) \((\d{1,3}(?:,\d{3})*) members and (\d{1,3}(?:,\d{3})*) guests\)"

            # Search for the pattern in the HTML content
            match = re.search(pattern, html_content)

            if match:
                # Extract the matched groups
                users = int(match.group(1).replace(",", ""))
                members = int(match.group(2).replace(",", ""))
                guests = int(match.group(3).replace(",", ""))
                print(f"Users: {users}, Members: {members}, Guests: {guests}")

                # Format the data
                timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                return [timestamp, users, members, guests]
            else:
                print("Pattern not found in the HTML content.")

        except Exception as e:
            print(f"Error fetching data: {e}")
            return None
        finally:
            browser.close()

def save_data(data):
    # Append data to a CSV file
    file_name = "data/dnd_usage.csv"
    with open(file_name, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(data)

if __name__ == "__main__":
    while True:
        data = fetch_data()
        if data:
            save_data(data)
            print("Data saved:", data)

        # Calculate randomized delay (1 hour ± a few minutes)
        delay = 3600 + random.randint(-120, 120)  # 1 hour ± 2 minutes
        print(f"Waiting for {delay // 60} minutes and {delay % 60} seconds...")
        time.sleep(delay)