"""
Задание 2.

Каждое из слов «class», «function», «method» записать в байтовом формате
без преобразования в последовательность кодов
не используя!!! методы encode и decode)
и определить тип, содержимое и длину соответствующих переменных.

Подсказки:
--- b'class' - используйте маркировку b''
--- используйте списки и циклы, не дублируйте функции
"""

name_1 = b"class"
name_2 = b"function"
name_3 = b"method"

name_list = [name_1, name_2, name_3]

for name in name_list:
    print(type(name), name, len(name))
