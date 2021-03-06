"""
Given an array of ints, return True if 6 appears as either the first or last element in the array. The array will be length 1 or more.


first_last6([1, 2, 6]) → True
first_last6([6, 1, 2, 3]) → True
first_last6([13, 6, 1, 2, 3]) → False"""

def first_last6(nums):
    return 6 in (nums[0],nums[-1])


print (first_last6([1, 2, 6]))
print (first_last6([6, 2, 6, 4]))
print (first_last6([15, 2, 6, 4]))