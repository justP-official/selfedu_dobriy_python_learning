"""
Подвиг 7. В функцию get_data() передается параметр value:

def get_data(value):
    match value:
        # здесь продолжайте программу

    return None
Необходимо дописать оператор match/case со следующими шаблонами:

* если переменная value имеет тип int и больше нуля, то вернуть значение переменной value;
* если переменная value имеет тип float и находится в диапазоне [-100; 100], то вернуть значение переменной value;
* если переменная value имеет тип str, то просто вернуть ее значение.
"""


def get_data(value):
    match value:
        case int() as int_value if int_value > 0:
            return int_value
        case float() as float_value if -100 < float_value < 100:
            return float_value
        case str() as str_value:
            return str_value

    return None
