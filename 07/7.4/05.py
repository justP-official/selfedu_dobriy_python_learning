def wrap_tag(s, tag='h1', up=True):
    return f"<{tag.upper()}>{s}</{tag.upper()}>" if up else f"<{tag}>{s}</{tag}>"


s = input()
print(wrap_tag(s, tag='div'))
print(wrap_tag(s, tag='div', up=False))
