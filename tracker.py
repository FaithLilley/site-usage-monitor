import requests
from bs4 import BeautifulSoup
import datetime
import csv

# URL of the website to scrape
URL = "https://www.dndbeyond.com/forums"

def fetch_data():
    try:
        # Fetch the webpage
        response = requests.get(URL)
        response.raise_for_status()  # Check for HTTP errors
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract data (adjust selectors based on website structure)
        online_users = soup.find('div', class_='online-users').text
        members = soup.find('div', class_='logged-in-users').text
        guests = soup.find('div', class_='guest-users').text

        # Format the data
        timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        return [timestamp, online_users, members, guests]

    except Exception as e:
        print(f"Error fetching data: {e}")
        return None

def save_data(data):
    # Append data to a CSV file
    file_name = "dnd_usage.csv"
    with open(file_name, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(data)

if __name__ == "__main__":
    data = fetch_data()
    if data:
        save_data(data)
        print("Data saved:", data)
