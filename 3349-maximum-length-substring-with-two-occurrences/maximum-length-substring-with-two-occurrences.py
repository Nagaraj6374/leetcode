class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        c={}
        l=0
        long=0
        for r in range(len(s)):
            c[s[r]]=c.get(s[r],0)+1
            while c[s[r]]>2:
                c[s[l]]-=1
                l+=1
            long=max(long,r-l+1)
        return long