n = int(input())

s = set()

for i in range(1, 11):
    if n % i == 0:
        s.add(i)

print("ДА" if {2, 3, 5} < s else "НЕТ")
