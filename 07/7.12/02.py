def wrap_in_tag(tag="h1"):
    def make_wrap(func):
        def wrapper(*args, **kwargs):
            res = func(*args)
            return f"<{tag}>{res}</{tag}>"
        return wrapper
    return make_wrap


@wrap_in_tag(tag='div')
def to_lower(s: str):
    return s.lower()


s = input()
print(to_lower(s))
