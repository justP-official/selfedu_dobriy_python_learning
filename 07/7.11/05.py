t = {'ё': 'yo', 'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ж': 'zh',
     'з': 'z', 'и': 'i', 'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p',
     'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'c', 'ч': 'ch', 'ш': 'sh',
     'щ': 'shch', 'ъ': '', 'ы': 'y', 'ь': '', 'э': 'e', 'ю': 'yu', 'я': 'ya'}


def replace_several_consecutive_hyphens(func):
    def wrapper(*args, **kwargs):
        res = func(*args)
        while "--" in res:
            res = res.replace("--", "-")
        return res
    return wrapper


@replace_several_consecutive_hyphens
def translate_to_eng(s):
    s = s.lower()
    res = ""
    for letter in s:
        if letter not in ": ;.,_":
            res += t.get(letter, letter)
        else:
            res += "-"
    return res


s = input()
print(translate_to_eng(s))
