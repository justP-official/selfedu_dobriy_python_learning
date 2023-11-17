import sys

# считывание списка из входного потока
lst_in = list(map(str.strip, sys.stdin.readlines()))

d = {}

for url in lst_in:
    if url in d:
        print(f"Взято из кэша: {d[url]}")
    else:
        d[url] = "HTML-страница для адреса" + url
        print(d[url])
