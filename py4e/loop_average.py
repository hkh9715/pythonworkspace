count = 0
sum = 0
print('Before', count, sum)
numbers = [9, 41, 12, 3, 74, 15]
for thing in numbers:
    count += 1
    sum += thing
    print(count, sum, thing)
print('After', count, sum, sum/count)
