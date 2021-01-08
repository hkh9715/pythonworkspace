#input 2
#output [2,4,6,8 cdots, 18]

def GuGu(n):
    result =[]
    i = 1
    while i < 10:
        result.append(n*i)
        i = i + 1
    return result

print(GuGu(2))


