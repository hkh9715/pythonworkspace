# condition
# cal1 = Calculator([1,2,3,4,5])
# cal1.sum()
# 15
# cal1.avg()
# 3.0
# cal2 = Calculator([6,7,8,9,10])
# cal2.sum()
# 40
# cal2.avg()
# 8.0

class Calculator:
    def __init__(self, listA):
        self.listA = listA
    def sum(self):
        result = 0
        for i in self.listA:
            result += i
        return result
    def avg(self):
        total = self.sum()
        result = total/len(self.listA)
        return result

cal1 = Calculator([1,2,3,4,5])
print(cal1.sum())
print(cal1.avg())

cal2 = Calculator([6,7,8,9,10])
print(cal2.sum())
print(cal2.avg())
