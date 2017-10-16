"""
Given 3 int values, a b c, return their sum. However, if one of the values is 13 then it does not count towards the sum and values to its right do not count. So for example, if b is 13, then both b and c do not count.


lucky_sum(1, 2, 3) → 6
lucky_sum(1, 2, 13) → 3
lucky_sum(1, 13, 3) → 1"""
def lucky_sum(a, b, c):
  sum = 0
  if (a ==13):
    return sum
  if (b == 13):
    return sum + a
  if (c == 13):
    return sum + b +a
  else:
    return a+b+c




print (lucky_sum(1, 2, 3))
print (lucky_sum(1, 2, 13))
print (lucky_sum(1, 13, 3))
print (lucky_sum(1, 13, 13))
print (lucky_sum(6, 5, 2))
print (lucky_sum(13, 2, 3))
print (lucky_sum(13, 2, 13))
print (lucky_sum(13, 13, 3))
print (lucky_sum(9, 4, 13))
print (lucky_sum(8, 13, 2))
print (lucky_sum(7, 2, 1))
print (lucky_sum(3, 3, 13))
