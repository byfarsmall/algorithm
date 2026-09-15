import re

S = input()
num = re.sub('[^0-9]', '', S)

print(num)