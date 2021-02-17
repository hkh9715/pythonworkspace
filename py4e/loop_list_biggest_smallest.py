smallest = None
biggest = None
# print('Before')
numbers = [9, 41, 12, 3, 74, 15]
for number in numbers:
    if smallest is None:
        smallest = number
    elif number < smallest:
        smallest = number
    if biggest is None:
        biggest = number
    elif number > biggest:
        biggest = number
print('smallest', smallest)
print('biggest', biggest)
