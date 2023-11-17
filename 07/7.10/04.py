def wrap_str(tag):
    def do_wrap(s):
        return f"<{tag}>{s}</{tag}>"

    return do_wrap


tag = input()
text = input()

wrapper = wrap_str(tag)
print(wrapper(text))
