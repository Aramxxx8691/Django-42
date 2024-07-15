import sys
import requests
from bs4 import BeautifulSoup

visited = []

def  roads_to_philosophy(page: str):
    wiki = "https://en.wikipedia.org"
    while True:
        url = wiki + page
        try:
            response = requests.get(url)
            response.raise_for_status()
        except:
            return print("It leads to a dead end!")
        soup = BeautifulSoup(response.text, 'html.parser')
        title = soup.find(id='firstHeading').text
        if title in visited:
            return print("It leads to an infinite loop!")
        visited.append(title)
        print(title)  
        if title == 'Philosophy':
            return print(f"{len(visited)} roads from {visited[0] if visited else 'Philosophy'} to Philosophy")
        content = soup.find(id='mw-content-text')
        if not content:
            return print("It leads to a dead end!")
        links = content.select('p > a')
        for link in links:
            href = link.get('href', '')
            if href.startswith('/wiki/') and not (href.startswith('/wiki/Wikipedia:') or href.startswith('/wiki/Help:')):
                return roads_to_philosophy(href)

def main():
    if len(sys.argv) == 2:
        try:
            roads_to_philosophy('/wiki/' + sys.argv[1].replace(' ', '_'))
        except Exception as e:
            print(f"❌ An error occurred: {e}")
    else:
        print("❌ Usage: python3 roads_to_philosophy.py <page>")

if __name__ == '__main__':
    main()