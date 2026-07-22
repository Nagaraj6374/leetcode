class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        r=0
        for i in range(len(s)-2):
            n=s[i:i+3]
            if len(set(n))==3:
                r+=1
        return r