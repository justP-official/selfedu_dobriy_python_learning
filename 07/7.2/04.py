def is_even(x):
    return True if x % 2 == 0 else False


while True:
    num = int(input())
    if num == 1:
        break

    if is_even(num):
        print(num)
        