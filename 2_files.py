"""
Домашнее задание №2

Работа с файлами


1. Скачайте файл по ссылке https://www.dropbox.com/s/sipsmqpw1gwzd37/referat.txt?dl=0
2. Прочитайте содержимое файла в перменную, подсчитайте длинну получившейся строки
3. Подсчитайте количество слов в тексте
4. Замените точки в тексте на восклицательные знаки
5. Сохраните результат в файл referat2.txt
"""

def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    with open('referat.txt', 'r', encoding = 'utf-8') as referat:
        context = referat.read()
        print(f'Длина строки: {len(context)}')
        count_words = context.split(' ')
        print(f'Всего слов в файле: {len(count_words)}')
        context = context.replace('.', '!')
        
    with open('referat_1.txt', 'w', encoding = 'utf-8') as referat_1:
        referat_1.write(context)



    

if __name__ == "__main__":
    main()
