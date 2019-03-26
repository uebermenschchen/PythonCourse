with open('rosalind_hamm.txt') as f:
    a=f.readline()
    b=f.readline()
res = [(x,y) for x,y in zip(a,b) if x != y]
print(len(res))
