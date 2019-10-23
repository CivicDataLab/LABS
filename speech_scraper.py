"""
Script for scraping Budget Speeches (India)

Usage:
    speech_scraper.py [--path=<p>]

Options:
    --path=<p>      Specify the path (Optional)
"""
from docopt import docopt
from typing import List
import requests
from bs4 import BeautifulSoup

BASE_URL = "https://www.indiabudget.gov.in/"

def construct_url():
    return BASE_URL + "bspeech.php"

def get_table():
    url = construct_url()
    page = requests.get(url)

    if page.status_code == 200:
        soup = BeautifulSoup(page.text, 'html.parser')
        table = soup.find('table')
        return table
    return "page is not available!"


if __name__ == "__main__":
    args = docopt(__doc__)

    path = args["--path"]

    table = get_table()

    for row in table.find_all('tr'):
        columns = row.find_all('td')
        for column in columns:
            try:
                url = column.find_all('a')[0]['href']
                if url.endswith('.pdf'):
                    response = requests.get(BASE_URL + url)
                    filename = column.find_all('a')[0].contents[0].replace(' ', '_')
                    if path:
                        filename = path + filename
                    # with open(filename + ".pdf", 'wb') as f:
                    #     f.write(response.content)
            except IndexError:
                pass
