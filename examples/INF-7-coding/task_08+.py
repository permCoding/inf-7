from itertools import product


al = '012'
lst = []
for word in product(al, repeat=3):
    lst.append( ''.join(word) )
print(len(lst), lst)
