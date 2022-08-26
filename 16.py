# Sample output: Counter({'a': 400, 'b': 400, 'd': 400, 'c': 300})

d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}
dic={}
for i,j in d1.items():
    for x,y in d2.items():
        if i==x:
            dic[i]=(j+y)
print(dic)
        
        
    


