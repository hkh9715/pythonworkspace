sh = input("Enter Hours: ")
sr = input("Enter Rate: ")

try:
    fh = float(sh)
    fr = float(sr)
except:
    print("Error, please enter numeric input")
    quit()

# print(fh, fr)
if fh>40:
    reg=fh*fr
    otp=(fh-40)*(fr*0.5)
    xp = reg + otp
else:
    xp = fh * fr
print("pay: ", xp)
