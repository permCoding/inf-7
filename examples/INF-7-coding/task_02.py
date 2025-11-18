tbl = {
    '000': 'А', 
    '010': 'Г', 
    '100': 'Р'
}

word = ''

code = '000010000100000010000100'

for i in range(0, len(code), 3):
    cd = code[i:i+3]
    ch = tbl[cd]
    word += ch

print(word)
