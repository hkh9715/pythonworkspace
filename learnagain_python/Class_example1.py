# output
# 박응용 부산여행을 가다.
# 김줄리엣 부산여행 3일 가네.
# 박응용, 김줄리엣 사랑에 빠졌네
# 박응용, 김줄리엣 결혼했네
# 박응용, 김줄리엣 싸우네
# 박응용, 김줄리엣 이혼했네

class HousePark:
    lastname = "박"
    def __init__(self, name):
        self.fullname = self.lastname + name
    def travel(self, where):
        print("%s %s여행을 가다." % (self.fullname, where))
    def love(self, other):
        print("%s, %s 사랑에 빠졌네" % (self.fullname, other.fullname))
    def __add__(self, other):
        print("%s, %s 결혼했네" % (self.fullname, other.fullname))
    def fight(self, other):
        print("%s, %s 싸우네" % (self.fullname, other.fullname))
    def __sub__(self, other):
        print("%s, %s 이혼했네" % (self.fullname, other.fullname))

class HouseKim(HousePark):
    lastname = "김"
    def travel(self, where, day):
        print("%s %s여행 %d일 가네." % (self.fullname, where, day))


pey = HousePark("응용")
juliet = HouseKim("줄리엣")
pey.travel("부산")
juliet.travel("부산", 3)
pey.love(juliet)
pey+juliet
pey.fight(juliet)
pey-juliet