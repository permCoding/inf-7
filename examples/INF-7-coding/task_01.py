tbl = {
    'А': '000', 
    'Г': '010', 
    'Р': '100'
}

word = 'ГАГАРА'

code = ''
for ch in word:
    code += tbl[ch]
print(code)
