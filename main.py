import json

import shops.shop as shop

def main():
    
    with open('products.json', 'r', encoding='utf-8') as products_json:
        products = json.load(products_json)

        for product in products:
            name        = product['Name']
            max_price   = product['MaxPrice']

            for shop_name, search in product['Shops'].items():
                try:
                    price = shop.get_product(shop_name, search)
                    # print(f'Search {name} in {shop_name} with max {max_price}. actual: {price}')
                    if price is None or price > max_price:
                        break
                    print(f'{name} in {shop_name} by {price} < {max_price}')

                except ValueError:
                    print('Fail')
    
if __name__ == '__main__':
    main()