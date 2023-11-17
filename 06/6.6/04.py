words = input().lower().split()

d = {word: words.count(word) for word in words}

print(d['и'])
