import requests
from bs4 import BeautifulSoup
import json

def scrape():
    #automatically scrape nyt for the letters
    URL = 'https://www.nytimes.com/puzzles/spelling-bee'
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')

    scripts = soup.find_all('script')[1].text[18:]
    dct = json.loads(scripts)

    outer_letters = dct['today']['outerLetters']
    center_letter = dct['today']['centerLetter']

    return (center_letter, outer_letters)


if __name__ == '__main__':
    print(scrape())