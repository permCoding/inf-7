f = open('./пляшущие_человечки.txt', mode='r', encoding='utf8')
s = f.read()

al = 'абвгдеёжзийклмнопрстуфхцчшщьыъэюя'

k = 0
for e in al: k += s.count(e)

for e in al: print(e, round(s.count(e) / k * 100, 2), '%')