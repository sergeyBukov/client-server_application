"""
Задание 4.

Преобразовать слова «разработка», «администрирование», «protocol»,
«standard» из строкового представления в байтовое и выполнить
обратное преобразование (используя методы encode и decode).

Подсказки:
--- используйте списки и циклы, не дублируйте функции
"""

name_1 = "разработка"
name_2 = "администрирование"
name_3 = "protocol"
name_4 = "standard"

name_list = [name_1, name_2, name_3, name_4]
print(f'Строковое представление: {name_list}')

list_byte = []
for name in name_list:
    z = name.encode(encoding="utf-8")
    list_byte.append(z)

print(f'Байтовое представление: {list_byte}')

list_str = []
for name in list_byte:
    z = name.decode(encoding="utf-8")
    list_str.append(z)

print(f'Обратное преобразование: {list_str}')
