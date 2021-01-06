class HousePark:
    lastname = "한"

    def __init__(self, name):
        self.fullname = self.lastname + name

    def travel(self, where):
        print("%s, %s여행을 가다." % (self.fullname, where))

# pey = HousePark("건희")
# pey.travel("영국")

class HouseKim(HousePark):
    lastname = "김"

    def travel(self, where, day):
        print("%s, %s여행 %d일 가네" % (self.fullname, where, day))

juliet = HouseKim("줄리엣")
juliet.travel("독도", 3)