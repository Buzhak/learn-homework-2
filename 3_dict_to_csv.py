import csv
"""

Домашнее задание №2

Работа csv

1. Создайте список словарей с ключами name, age и job и значениями по вашему выбору. 
   В списке нужно создать не менее 4-х словарей
2. Запишите содержимое списка словарей в файл в формате csv

"""
users = [
    {'name': 'Петя', 'age': '21', 'job': 'CNC operator'},
    {'name': 'Вася', 'age': '24', 'job': 'waiter'},
    {'name': 'Юля', 'age': '29', 'job': 'manager'},
    {'name': 'Серёжа', 'age': '32', 'job': 'manager'}
]


def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    with open('dict.csv', 'w', encoding = 'utf-8', newline = '') as dict:
        fields = ['name', 'age', 'job']
        writer = csv.DictWriter(dict, fields, delimiter = ';')
        writer.writeheader()
        for user in users:
            writer.writerow(user)

if __name__ == "__main__":
    main()
