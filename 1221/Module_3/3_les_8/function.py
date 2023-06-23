# if __name__ == "__main__":
#
#     goods = [
#         {
#             'name': 'Iphone 7',
#             'brand': 'Apple',
#             'price': 100,
#         },
#         {
#             'name': 'Ipad',
#             'brand': 'Apple',
#             'price': 50,
#         },
#         {
#             'name': 'Windows XP',
#             'brand': 'Microsoft',
#             'price': 150,
#         }
#     ]
#
#
#     def on_price(item):
#         return item['price']
#
#
#     print(sorted(goods, key=lambda item: item['price']))
#
#     filtered_list = list(filter(lambda item: item['brand'] == 'Apple', goods))
#     print(filtered_list)
#
#     numbers = ['1', '2', '3', '4', '5']
#     result = list(map(int, numbers))
#     print(result)
#
#
#     names_list = ['Igor', 'Артем', 'Аня', 'Ксюша']
#     surnames = ['Ivanov', 'Petrovich', 'Maksimova', 'Andreevna']
#
#     persons = list(map(lambda name, surname: f'{name} {surname}', names_list, surnames))
#     print(persons)
#
#     new_goods = []
#
#     for index, item in enumerate(goods):
#         print(index)
#         new_goods.append({index: item})
#
#     print(new_goods)
#
#     for name, surname in zip(names_list, surnames):
#         print(name, surname)
#
#
# else:
#     print("Скрипт запустился из вне")



names_list = ['данил', 'артём', 'никита', 'влад']
result = list(map(lambda name: name.title(), names_list))
print(result)