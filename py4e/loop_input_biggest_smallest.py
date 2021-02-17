bb = None
ss = None
while True:
    num = input("Enter a number: ")
    if num == "done" : break
    try:
        inum = float(num)
        if bb is None:
            bb=inum
        elif inum>bb:
            bb=inum
        if ss is None:
            ss=inum
        elif inum<ss:
            ss=inum
    except:
        print('invalid input')
        continue

print("Maximum is ", bb)
print("Minimum is ", ss)
