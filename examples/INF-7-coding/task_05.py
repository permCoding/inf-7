tbl = {
    'К': '00', 
    'Л': '01', 
    'М': '10', 
    'О': '11'
}

word = 'МОЛОКО'

code = ''
for ch in word:
    code += tbl[ch]
print(code)
