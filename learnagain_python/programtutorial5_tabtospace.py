# input : file that contains tab contents
# output : file that contains space contents
# function : f.read(), replace()

#python bbb.py src dst
import sys

a = sys.argv[1]
b = sys.argv[2]

f = open(a)
tab_content = f.read()
f.close()

space_content = tab_content.replace("\t", " "*4)
print(space_content)
# f = open(b, 'w')
# f.write(space_content)
# f.close()