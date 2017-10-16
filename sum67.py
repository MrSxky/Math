"""List-2 > sum67
prev  |  next  |  chance
Return the sum of the numbers in the array, except ignore sections of numbers starting with a 6 and extending to the next 7 (every 6 will be followed by at least one 7). Return 0 for no numbers.


sum67([1, 2, 2]) → 5
sum67([1, 2, 2, 6, 99, 99, 7]) → 5
sum67([1, 1, 6, 7, 2]) → 4"""

def sum67(nums):
    flag=False
    sum=0

    for num in nums:
        if(num==6):                  #Turn the flag on if the number is 6
            flag=True
            continue
        if(num==7 and flag is True): #Turn the flag Off when 7 is seen after 6
            flag=False
            continue
        if(flag is False):           #Keep on adding the nums otherwise
            sum+=num
    return sum

print (sum67([1, 2, 2, 6, 99, 99, 7]) )
print (sum67([6, 8, 1, 6, 7]))
print (sum67([1, 6, 7, 7]) )