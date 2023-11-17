marks = input().split()
start = int(marks.pop(0))

d = {start + i: marks[i] for i in range(len(marks))}
print(d[4])
