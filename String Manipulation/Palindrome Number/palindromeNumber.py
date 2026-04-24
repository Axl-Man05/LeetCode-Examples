class Solution:
    def isPalindrome(self, x: int) -> bool:
        if(x < 0):
            return False
        textNumber = str(x)
        n = -1
        for i in textNumber:
            if(i == textNumber[n]):
                n-=1
            else:
                return False
        return True

"""
Best solution in ms:
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        s = str(x)
        return s == s[::-1]
"""

