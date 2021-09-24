import json

import shops.shop as shop

def main():
    
    with open('products.json', 'r', encoding='utf-8') as products_json:
        products = json.load(products_json)

        for product in products:
            name        = product['Name']
            max_price   = product['MaxPrice']
            # print(product['Name'])
            # print()

            for product_shop in product['Shops']:
                shop_name   = product_shop['Name']
                search      = product_shop['SearchValue']

                try:
                    price = shop.get_product(shop_name, search)
                    if price is None or price > max_price:
                        break
                    print(name, shop_name, price)
                    print()

                except ValueError:
                    print('Fail')
    
if __name__ == '__main__':
    main()