def wrap_str():
    def do_wrap(s):
        return f"<h1>{s}</h1>"

    return do_wrap


wrapper = wrap_str()
print(wrapper(input()))
