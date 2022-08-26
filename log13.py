# 0/p expect result:-['e','b','c']

my_dict = {'a':50, 'b':58, 'c':56,'d':40, 'e':100, 'f':20}
from collections import Counter
k = Counter(my_dict)
high = k.most_common(5)
for i in high:
    print(i[0])
