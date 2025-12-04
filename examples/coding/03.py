s = open('./пляшущие_человечки.txt', 'r', encoding='utf8').read()

al = 'абвгдеёжзийклмнопрстуфхцчшщьыъэюя'

k = 0
for e in al: k += s.count(e)

lst = []
for e in al: 
    lst.append( [e, round(s.count(e) / k * 100, 2)] )

lst.sort(key=lambda x: x[1], reverse=True)

for i, e in enumerate(lst, start=1): 
    print(str(i).rjust(2), e[0].rjust(3), str(e[1]).rjust(7), '%', sep=' ')
