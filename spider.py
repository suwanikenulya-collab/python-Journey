import requests
from bs4 import BeautifulSoup
from urllib import *

visited_urls= set()

def spider_urls(url, keywords):
    try:
        response = requests.get(url)
    except:
        print(f"Request failed {url}")
        return

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')

        links = soup.find_all('a')
        urls= []
        for tag in links:
            href = tag.get("href")
            if href is not None and href !="":
                urls.append(href)
        print(urls)




url=input("enter the url you want to scrap. ")
keywords = input("enter the keywords you want to scrap. ")
spider_urls(url, keywords)
