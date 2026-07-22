class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        c = 0
        d = 10 ** k
        n = num
        while num >= 10 ** (k - 1):
            sub = num % d
            if sub != 0 and n % sub == 0:
                c += 1
            num //= 10 
        return c