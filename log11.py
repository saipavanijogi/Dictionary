# 3 highst vaues( 50,58,100)
my_dict = {'a':50, 'b':58, 'c':56,'d':40, 'e':100, 'f':20}
from collections import Counter
k = Counter(my_dict)
high = k.most_common(3)
for i in high:
   print(i[1])
