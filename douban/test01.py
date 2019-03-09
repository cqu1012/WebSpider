# -*- coding: utf-8 -*-
import re
A = 'a33aa2a3aa5aa6aaa3aaa7aaa8aaa4'

#第一题
# A=re.findall('a+',A)
# print(A)
#第二题
# str2 = re.findall(r'\d+',A)
# print(str2)

#第三题
def compare(numStr1,numStr2):
    a1Num = len(list(re.findall('a+',numStr1)[0]))
    d1Num = int(re.findall('\d+',numStr1)[0])
    a2Num = len(list(re.findall('a+', numStr2)[0]))
    d2Num = int(re.findall('\d+', numStr2)[0])
    if a1Num < a2Num:
        return False
    elif a1Num==a2Num:
        if d1Num <= d2Num:
            return False
        else:
            return True
    else:
        return True

str1 = re.findall(r'a+\d+',A)
print('排序前：')
print(str1)
for i in range(len(str1)):
    a = str1[0]
    num  = 0
    for str in str1:
        flag = compare(a,str)
        if flag and num > 0:
            str1[num-1],str1[num] = str1[num],str1[num-1]
        a = str
        num +=1
print('排序后：')
print(str1)

