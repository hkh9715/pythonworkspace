# input : 0123456789 01234 01234567890 6789012345 012322456789
# output : true false false true false
# function : append, len

def chkDupNum(s):
    result=[]
    for num in s:
        if num not in result:
            result.append(num)
        else:
            return False
    return len(result)==10

print(chkDupNum("0123456789"))
print(chkDupNum("01234"))

# def chkDupNum(s):
#     result=[]
#     for block in s.split(" "):
#         for num in s:
#             if num not in result:
#                 result.append(num)
#             else:
#                 return False
#         return len(result)==10
#     return 

# print(chkDupNum("0123456789 01234 01234567890 6789012345 012322456789"))