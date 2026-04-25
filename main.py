import requests
from bs4 import BeautifulSoup

def get_page(url):
    try:
        headers = {
            "User-Agent": "Mozilla/5.0"
        }

        response = requests.get(url, headers=headers)
        response.raise_for_status()  # raises error if request fails

        soup = BeautifulSoup(response.content, 'html.parser')

        if soup.title:
            print(soup.title.string)
        else:
            print("No title found")

    except requests.exceptions.RequestException as e:
        print("Error:", e)


get_page(input("What URL would you like to scrape: "))