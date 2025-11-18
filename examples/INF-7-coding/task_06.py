tbl = {
    '00': 'Б', 
    '01': 'Д', 
    '10': 'Р',
    '11': 'О'
}

word = ''

code = '0111001011'

for i in range(0, len(code), 2):
    cd = code[i:i+2]
    ch = tbl[cd]
    word += ch

print(word)
