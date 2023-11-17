def show_menu(func):
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        for i, item in enumerate(res):
            print(f"{i+1}. {item}")
    return wrapper


@show_menu
def get_menu(s):
    return s.split()
