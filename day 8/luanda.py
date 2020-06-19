class Time:
    def __init__(self, t):
        self.h, self.m = map(int, t.split(':'))
        self.str = t

    def __repr__(self):
        return self.str

    def __lt__(self, other):
        if self.h == other.h:
            return self.m < other.m
        else:
            return self.h < other.h

    def __eq__(self, other):
        if type(other) == Time:
            return self.str == other.str
        return False

    def __gt__(self,other):
        if self.h == other.h:
            return self.m > other.m
        else:
            return self.h > other.h

n = int(input())

first_seen = Time("19:00")
last_seen = Time("6:30")

six = Time("6:30")
nineteen = Time("19:00")

for i in range(n):

    time = Time(input())

    if time < six or time > nineteen:
        continue

    if time < first_seen or time == first_seen:
        first_seen = time

    if time > last_seen or time == last_seen:
        last_seen = time



if first_seen > Time("6:29") and first_seen < Time("10:01"):
    if (last_seen > Time("6:29") and last_seen < Time("16:01")):
        print(24000)

    elif (last_seen > Time("16:00") and last_seen < Time("19:01")):
        print(36000)

elif (first_seen > Time("10:00") and first_seen < Time("16:01")) and (last_seen > Time("10:00") and last_seen < Time("16:01")):
    print(16800)

elif (first_seen > Time("10:00") and first_seen < Time("19:01")) and (last_seen > Time("16:00") and last_seen < Time("19:01")):
    print(24000)
else:
    print(0)
