def wrap_tag(s, tag='h1'):
    return f"<{tag}>{s}</{tag}>"


s = input()
print(wrap_tag(s))
print(wrap_tag(s, tag='div'))