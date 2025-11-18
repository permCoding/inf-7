tbl = {
    '00': 'А', 
    '01': 'Г', 
    '10': 'Р'
}

word = ''

code = '0001001000010010'

for i in range(0, len(code), 2):
    cd = code[i:i+2]
    ch = tbl[cd]
    word += ch

print(word)
