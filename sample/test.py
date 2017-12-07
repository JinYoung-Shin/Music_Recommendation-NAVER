import re

str = '(MR B1) 너의 의미 - 아이유 (Feat. 김창완)'

q = re.sub('\([^()]+\)', '', str)
q = re.sub('\-.*','',q)



print(str.find('아이오'))


dic = {'key':'1','key1':'2'}

print (next(iter(dic)))