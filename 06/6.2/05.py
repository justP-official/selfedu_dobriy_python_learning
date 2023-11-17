things = {'карандаш': 20, 'зеркальце': 100, 'зонт': 500, 'рубашка': 300,
          'брюки': 1000, 'бумага': 200, 'молоток': 600, 'пила': 400, 'удочка': 1200,
          'расческа': 40, 'котелок': 820, 'палатка': 5240, 'брезент': 2130, 'спички': 10}

n = float(input()) * 1000

current_weight = 0

bag = []

d = {v: k for k, v in things.items()}


while current_weight <= n:
    if len(d.keys()) > 0:
        heaviest = max(d.keys())
        if current_weight + heaviest <= n:
            current_weight += heaviest
            bag.append(d[heaviest])
        d.pop(heaviest)
    else:
        break

print(*bag)
