import os

path = os.path.join('modifications.txt')

file=open(path,"r")
contents=file.read()
all=contents.split()
table=all[0]
Operations=all[1]
print(Operations)
contents.close()