class FourCal: 
    def setdata(self, first, second):    #객체에 연산할 숫자 지정할 수 있게 만들기 
        self.first = first
        self.second = second

    def add(self):    #더하기 기능 구현
        result = self.first + self.second
        return result

a = FourCal()
a.setdata(4, 2)
a.add()
print(a.add())

# class FourCal:
    
#     def __init__(self, first, second):
#         self.first = first
#         self.second = second

#     def setdata(self, first, second):
#         self.first = first
#         self.second = second

#     def add(self):
#         result = self.first + self.second
#         return result

# a = FourCal(4, 2)
# a.add()