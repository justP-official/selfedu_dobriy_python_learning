"""
Подвиг 4. Вводится строка из слов, записанных через пробел.
Необходимо на их основе составить прямоугольную таблицу из трех столбцов и N строк
(число строк столько, сколько получится). Лишнее (выходящее) слово - отбросить.
Реализовать эту программу с использованием функции zip.
Результат отобразить на экране в виде прямоугольной таблицы из слов, записанных через пробел (в каждой строчке).
"""

cities = iter(input().split())

cities = zip(cities, cities, cities)

for city in cities:
    print(*city)
