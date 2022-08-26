
    
d={"d1":[1,2,3],"d2":[4,5,6],"d3":[7,8,9],}
i=0
b=0
c=0
while i<len(d):
    for values in d:
        b=sum(d[values]) 
        c=c+b
        i=i+1
    print(c)  