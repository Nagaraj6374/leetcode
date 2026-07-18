class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        c={}
        for char in s:
            c[char]=c.get(char,0)+1
        for char in t:
            if char not in c or c[char]==0:
                return False
            c[char]-=1
        return True