class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0: return False
        return self.reverse(x) == x
    
    def reverse(self, x):
        y = 0
        while x:
            d = x % 10
            y = y * 10 + d
            x //= 10
        return y