t = {'ё': 'yo', 'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ж': 'zh',
     'з': 'z', 'и': 'i', 'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p',
     'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'c', 'ч': 'ch', 'ш': 'sh',
     'щ': 'shch', 'ъ': '', 'ы': 'y', 'ь': '', 'э': 'e', 'ю': 'yu', 'я': 'ya'}


def replacer_wrap(chars=" !?"):
    def replace_chars(func):
        def wrapper(*args, **kwargs):
            res = func(*args)
            for char in chars:
                while char in res:
                    res = res.replace(char, "-")

            while "--" in res:
                res = res.replace("--", "-")

            return res
        return wrapper

    return replace_chars


@replacer_wrap(chars="?!:;,. ")
def translate_to_eng(text):
    text = text.lower()
    res = ""

    for letter in text:
        res += t.get(letter, letter)

    return res


s = input()
print(translate_to_eng(s))
