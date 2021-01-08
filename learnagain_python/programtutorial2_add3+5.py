# input 1~999 (integar)
# output sum of 'multiples of 3 and multiples of 5'

# def multiple(n):
#     result = []
#     for i in range(1, 1000):
#         if i % 3 ==0:
#             result.append(i)
#     return result

# # multiple(3) = [3,6,9,cdots,999] #multiples of 3
# # multiple(5) = [5,10,15,cdots,995] #multiples of 5
# # result = sum(result1) + sum(result2)

# print(sum(multiple(3)))

result = 0
for n in range(1, 1000):
    if n % 3 == 0 or n % 5 == 0:
        result += n
print(result)