# Sample Dictionary ( n = 5) :
# Expected Output : {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
from re import I


dic={}
for i in range(1,6):
   dic[i]=i*i              
print(dic)