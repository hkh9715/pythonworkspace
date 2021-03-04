#review dictionary concept

a = {1: 'a'}
a[2] = 'b'
# print(a)

del a[1]
# print(a)
# print(a['b'])

# b= {[1, 2]:'hi'}
# print(b)

c = {'name':'pey', 'phone':'1234567890', 'birth':'1118'}
# print(c.keys())
# print(list(c.keys()))
# for k in c.keys():
    # print(k)

# print(c.values())
# print(c.items())


# a.clear()
# print(a)


# print(c.get('what'))
# print(c.get('what', 'bar')) #default value
# c['what']


print('name' in c)