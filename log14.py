#0/p{'param':20,'anjili':30,'bijender':45,'roshini':50,'deepak':60}
a={'bijender':45,'deepak':60,'param':20,'anjili':30,'roshini':50}
import operator
b = dict(sorted(a.items(),key=operator.itemgetter(1)))
print(b)




# sorted_d = dict( sorted(a.items(), key=operator.itemgetter(1),reverse=True))
# print('Dictionary in descending order by value : ',sorted_d)
