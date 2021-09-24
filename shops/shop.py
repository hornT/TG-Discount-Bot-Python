import json

import shops.metro as metro

get_products = {
    'Metro': metro.get_product
}

shop_urls = {}
with open('shops.json', 'r', encoding='utf-8') as shops_json:
        shop_urls = json.load(shops_json)

def get_product(shop_name, search):
    shop_get_product = get_products.get(shop_name)

    if shop_get_product is not None:
        url = shop_urls[shop_name]

        return shop_get_product(url, search)

    return None