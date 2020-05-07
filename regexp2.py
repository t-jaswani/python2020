# REG EXPRESSION TO FIND ALL WORDS STARTING WITH AK OR AN

import re
str = 'anil akhil anant arun ararti arundhati abhijit ankur'
res = re.findall (r'a[nk][\w]*', str)
print(res)