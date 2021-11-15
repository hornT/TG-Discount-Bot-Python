from bs4 import BeautifulSoup
import urllib.request


def get_product(url, search):

    req = urllib.request.Request(
        url + search,
        data=None,
        headers={
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
        }
    )
    try:

        html_doc = urllib.request.urlopen(req).read()
        soup = BeautifulSoup(html_doc, features="html.parser")

        primary_prices = soup.find('div', 'price-label--primary')
        price = primary_prices.find('span', 'price-label__integer')

        return int(price.contents[0].strip())
    except Exception as error:
        print(error)