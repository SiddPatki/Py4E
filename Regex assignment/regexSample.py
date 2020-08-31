import re

f=open("regex_sum_916965.txt","r")
x=f.read()
y=list(map(lambda x: int(x) ,re.findall("[0-9]+",x)))
print(sum(y))