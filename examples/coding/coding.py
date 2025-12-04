# from random import shuffle
alph = 'абвгдеёжзийклмнопрстуфхцчшщьыъэюя'
# code = list(alph)
# print(code)
# shuffle(code)
# print(code)
# print(''.join(code))
code = 'ющъслзбёыншухпжэтьиевймярадгцчфко'

lines = open('./input.txt').readlines()

with open('./output.txt', 'w', encoding='utf') as f:
    for line in lines:
        line = line.strip()
        s = ''
        for e in line:
            if alph.find(e) > -1:
                s += code[alph.index(e)]
            else:
                s += e
        f.write(s + '\n')
        print(s)