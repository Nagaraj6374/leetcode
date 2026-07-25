class Solution:
    def maxProduct(self, n: int) -> int:
        digits = sorted(map(int, str(n)))
        return digits[-1] * digits[-2]