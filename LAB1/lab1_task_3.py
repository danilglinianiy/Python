import random

items = list(range(1000))

random.shuffle(items)
print(items[:10])

print('Minimal number: ', min(items[:10]))
