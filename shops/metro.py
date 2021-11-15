import requests


def get_product(url, search):
    try:
        response = requests.get(url + search)
        response.raise_for_status()

        result = response.json()

        return result['data']['data'][0]['prices']['price']
    except requests.exceptions.HTTPError as error:
        print(error)
