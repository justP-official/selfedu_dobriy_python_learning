"""
Подвиг 5. Вводится список email-адресов в одну строчку через пробел.
Среди них нужно оставить только корректно записанные адреса.
Будем полагать, что к таким относятся те, что используют латинские буквы, цифры и символ подчеркивания.
А также в адресе должен быть символ "@", а после него символ точки "."
(между ними, конечно же, могут быть и другие символы).

Результат отобразить в виде строки email-адресов, записанных через пробел.
"""

import string

chars = string.ascii_lowercase + string.digits + "_"


def validate_email(email):
    if "@" in email:
        part_one, part_two = email.split("@")
        if "." in part_two:
            for char in part_one:
                if char not in chars:
                    return False
            else:
                return True

    return False


res = tuple(filter(validate_email, input().split()))

print(" ".join(res))
