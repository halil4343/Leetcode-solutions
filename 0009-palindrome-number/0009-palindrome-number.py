class Solution:
    def isPalindrome(self, x: int) -> bool:
        st = str(x)
        rev = st[::-1]
        if rev==st:
            return True
        else:
            return False
        