cabinet = {"A-3":"유재석", "B-100":"김태호"}
# print(cabinet[3])
# print(cabinet.get(3))

# print(cabinet)
cabinet["A-3"] = "김종국"
cabinet["C-20"] = "조세호"
cabinet["B-99"] = "지석진"
# print(cabinet)

del cabinet["A-3"]
# print(cabinet)

#print(cabinet.keys())
#print(cabinet.values())
cabinet.clear()
print(cabinet)