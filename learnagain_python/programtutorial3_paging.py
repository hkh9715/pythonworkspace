# input number of 게시물(m), 한 페이지에 보여줄 게시물 수(n) 
# output total number of pages

def getTotalPage(m, n):
    if m % n == 0:
        return m//n
    else:
        return m//n + 1

print(getTotalPage(5,10))
print(getTotalPage(15,10))
print(getTotalPage(25,10))
print(getTotalPage(30,10))
