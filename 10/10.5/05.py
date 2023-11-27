"""
Подвиг 5. Вводятся данные по книге в виде строки через запятую в формате (некоторые значения могут отсутствовать):

id, автор, название, цена, год издания

с помощью команд:

t = (int, str, str, float, int)
book = [t[i](x) if t[i] != str else x.strip() for i, x in enumerate(input().split(","))]
Например, при вводе:

"1, Балакирев С.М., Python, 2100, 2023"

получим список:

book = [1, 'Балакирев С.М.', 'Python', 2100.0, 2023]

А при вводе:

"1, Балакирев С.М., Python"

список:

book = [1, 'Балакирев С.М.', 'Python']

И так далее.

С помощью оператора match/case необходимо определить шаблоны для выделения следующей информации с дополнительными проверками:

автор, название (автор - не менее 6 символов, название - не менее 10 символов)
автор, название, цена (автор не менее 6 символов, цена - положительное число)
автор, название, год издания (год издания от 2020 и выше)
автор, название, цена, год издания (цена - положительное число и год издания от 2020 и выше)

Первый шаблон срабатывает, если есть только автор и название;
второй, если появляется еще и цена;
третий, если есть автор, название, год издания, но нет цены;
последний, если имеются все данные.

При срабатывании шаблона вывести на экран строку "Yes". Если ни один из шаблонов не сработал, то вывести строку "No".
"""

t = (int, str, str, float, int)
book = [t[i](x) if t[i] != str else x.strip() for i, x in enumerate(input().split(","))]

match book:
    case _, str() as autor, str() as title if len(autor) > 6 and len(title) > 10:
        print("Yes")
    case _, str() as autor, str() as title, float() as price if len(autor) > 6 and price > 0:
        print("Yes")
    case _, str() as autor, str() as title, int() as year if year >= 2020:
        print("Yes")
    case _, str() as autor, str() as title, float() as price, int() as year if price > 0 and year >= 2020:
        print("Yes")
    case _:
        print("No")
