def create_collection(tp):
    def do_creation(s):
        nonlocal tp
        return list(map(int, s.split())) if tp == 'list' else tuple(map(int, s.split()))

    return do_creation


tp = input()
cc = create_collection(tp)
lst = cc(input())
print(lst)
