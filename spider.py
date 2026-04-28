from urllib.parse import urljoin
import requests
from bs4 import BeautifulSoup

visited_urls = set()

def spider_urls(url, keywords):
    if url in visited_urls:
        return

    print("Visiting:", url)
    visited_urls.add(url)

    try:
        response = requests.get(url)
        response.raise_for_status()
    except:
        print(f"Request failed {url}")
        return

    soup = BeautifulSoup(response.content, 'html.parser')

    links = soup.find_all('a')

    for tag in links:
        href = tag.get("href")

        if href:
            full_url = urljoin(url, href)

            if full_url not in visited_urls:
                print(full_url)
                spider_urls(full_url, keywords)


url = input("Enter the URL: ")
keywords = input("Enter keywords: ")

spider_urls(url, keywords)