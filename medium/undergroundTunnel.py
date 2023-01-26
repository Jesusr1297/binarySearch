"""


Implement a data structure with the following methods:

void checkIn(int userId, String station, int timestamp) which
means user userId checked in to station station at time timestamp.
A user can only be checked in at one station at a time.

void checkOut(int userId, String station, int timestamp) which
means user userId checked out of station station at time timestamp.

float averageTime(String start, String end) returns the average time
for a person to move between station start and end.

You can assume that for a given user, checkIn always occurs before checkOut.
Also, averageTime will only be called if at least one person travelled
between the two stations.

Constraints
0 ≤ n ≤ 100,000 where n is the number of calls to checkIn, checkOut and averageTime.

"""


class UndergroundTunnel:
    def __init__(self):
        self.users = {}

    def checkIn(self, userId, station, timestamp):
        self.users[userId] = {'checkIn': {'station': station, 'time': timestamp}}
        return

    def checkOut(self, userId, station, timestamp):
        self.users[userId] = {'checkOut': {'station': station, 'time': timestamp}}
        return

    def averageTime(self, start, end):
        times = []
        for user in self.users:
            try:
                times.append(user['checkIn'][start] - user['checkOut'][end])
            except:
                pass
        return sum(times)/len(times)
