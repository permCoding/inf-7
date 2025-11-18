tbl = {
    '00': 'Б', 
    '01': 'Д', 
    '10': 'Р',
    '11': 'О'
}

word = ''

code = '0111001011'
while len(code) > 0:
    cd = code[:2]
    ch = tbl[cd]
    word += ch
    code = code[2:]

print(word)
