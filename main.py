import json

import shops.shop as shop


def main():
    with open('products.json', 'r', encoding='utf-8') as products_json:
        products = json.load(products_json)
        shops = shop.get_products.keys()

        for product in products:
            name = product['Name']
            max_price = product['MaxPrice']

            for shop_name in shops:
                search = product.get(shop_name)
                if search is None:
                    continue
                try:
                    price = shop.get_product(shop_name, search)
                    if price is None or price > max_price:
                        break
                    print(f'{name} in {shop_name} by {price} < {max_price}')
                except Exception as ex:
                    print(f'Fail {ex}')


if __name__ == '__main__':
    main()
