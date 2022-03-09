import re


a = "abcdefg"
p = re.compile('[a-zA-Z]{1,5}')
b = p.findall(a)
b = ''

print(str(b))