"""We want make a package of goal kilos of chocolate. We have small bars (1 kilo each) and big bars (5 kilos each). Return the number of small bars to use, assuming we always use big bars before small bars. Return -1 if it can't be done.


make_chocolate(4, 1, 9) → 4
make_chocolate(4, 1, 10) → -1
make_chocolate(4, 1, 7) → 2"""


def make_chocolate(small, big, goal): #comments for the first example
    maxBig = goal // 5  #( 9//5 is 1) (10//5 is 2)  ((7//5) is 1)

    if small + big * 5 < goal or small < goal % 5: #( 4+ (1*5)=9 < 9 or 4< (9%5) = 4 In the second example
        return -1
    elif big >= maxBig: #1>=1
        return goal - maxBig * 5 # 9-1*5 = 4
    elif big <= maxBig: #case 3 (1 <= 1
        return goal - big * 5 

print (make_chocolate(4,1,9))
print (make_chocolate(4,1,10))
print (make_chocolate(4,1,7))