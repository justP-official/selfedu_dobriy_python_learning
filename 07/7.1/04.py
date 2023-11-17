def check_list(lst):
    print(f"Min = {min(lst)}, max = {max(lst)}, sum = {sum(lst)}")


a = [int(x) for x in input().split()]

check_list(a)
