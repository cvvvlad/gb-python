# Реализовать структуру данных «Товары». Она должна представлять собой список кортежей.
# Каждый кортеж хранит информацию об отдельном товаре.
# В кортеже должно быть два элемента — номер товара и словарь с параметрами,
# то есть характеристиками товара: название, цена, количество, единица измерения.
# Структуру нужно сформировать программно, запросив все данные у пользователя

# Нужно собрать аналитику о товарах.
# Реализовать словарь, в котором каждый ключ — характеристика товара, например, название.
# Тогда значение — список значений-характеристик, например, список названий товаров.

products = []
product = {}
while True:
    key = input("Характеристика товара"
                "\nили [+] для добавления товара"
                "\nили [Enter] 2 раза для получения аналитики:")

    add_product = False
    end = False

    if not key:
        add_product = True
        end = True

    if key == '+':
        add_product = True

    if add_product:
        products.append((len(products)+1, product))
        product = {}

    if end:
        break

    if not add_product and not end:
        value = input("Значение характеристики:")
        product[key] = value

print(f"\nВведенные товары:{products}")

analytics = {}
for item in products:
    product = item[1]
    for key in product:
        if not any(x == key for x in analytics.keys()):
            analytics[key] = []
        value = product[key]
        if not any(x == value for x in analytics[key]):
            analytics[key].append(value)

print(f"Аналитика:{analytics}")
