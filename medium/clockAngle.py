"""

Given a clock time with hour and integer minutes,
determine the smaller angle between the hour and
the minute hands and floor it to the nearest integer.

Note that the hour hand moves too.

Bonus: When, during the course of a day, will the angle be zero?

Constraints
0 ≤ hour ≤ 23
0 ≤ minutes ≤ 59

"""


def solve(hour, minutes):
    angle_minutes_from_zero = 6 * minutes
    angle_hour_from_zero = (30 * (hour % 12) + 0.5 * minutes)
    angle = abs(angle_hour_from_zero - angle_minutes_from_zero)

    return int(360 - angle) if angle > 180 else int(angle)


hour = 12
minutes = 22
assert solve(hour, minutes) == 121

hour = 18
minutes = 0
assert solve(hour, minutes) == 180

hour = 10
minutes = 0
assert solve(hour, minutes) == 60

hour = 23
minutes = 7
assert solve(hour, minutes) == 68


hour = 19
minutes = 53
assert solve(hour, minutes) == 81

