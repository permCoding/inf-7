f = open('./пляшущие_человечки.txt', mode='r', encoding='utf8')
s = f.read()

al = 'абвгдеёжзийклмнопрстуфхцчшщьыъэюя'

for e in al:
    print(e, s.count(e))
