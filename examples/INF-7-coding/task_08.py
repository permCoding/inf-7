from itertools import product

count = 0
al = '@#&'
for word in product(al, repeat=3):
    count += 1
    print(count, word)  # 27
