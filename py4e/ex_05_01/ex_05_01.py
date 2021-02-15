count = 0
tot = 0
while True :
    sval = input('Enter a number: ')
    if sval == 'done':
        break
    try :
        fval = float(sval)
    except :
        print('Invalid input')
        continue
    count += 1
    tot += fval

print(tot, count, tot/count)
