"""
Given a string, return a new string where the first and last chars have been exchanged.


front_back('code') → 'eodc'
front_back('a') → 'a'
front_back('ab') → 'ba'"""

def front_back(str):
    return str[::-1]

print (front_back('code'))
print (front_back('lana'))
print (front_back('nigga'))

