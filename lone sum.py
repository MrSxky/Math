"""
Given 3 int values, a b c, return their sum. However, if one of the values is the same as another of the values, it does not count towards the sum.


lone_sum(1, 2, 3) → 6
lone_sum(3, 2, 3) → 2
lone_sum(3, 3, 3) → 0"""


def lone_sum(a, b, c):
    sum = 0
    if (a == b == c):
        return sum
    if (a == b):
        return sum + c
    if (a == c):
        return sum + b
    if (b == c):
        return sum + a

    else:
        return a + b + c

print (lone_sum(1, 2, 3))
print (lone_sum(3, 2, 3))
print (lone_sum(3, 3, 3))
print (lone_sum(1, 3, 3))