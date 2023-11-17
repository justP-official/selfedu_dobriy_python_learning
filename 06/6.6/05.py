import sys

# считывание списка из входного потока
lst_in = list(map(str.strip, sys.stdin.readlines()))

new_lst_in = [[s for s in x.split(': ')] for x in lst_in]
authors = [author[0] for author in new_lst_in]
# authors = [x.split(': ') for x in lst_in]

# books = [book[1:] for book in lst_in]

# d = dict().fromkeys(authors, {})
d = {}
for item in new_lst_in:
    if item[0] not in d:
        d[item[0]] = {item[1]}
    d[item[0]].add(item[1])

print(d)
# print(new_lst_in)
