class Solution:
    def isValid(self, s):
        brackets,l,r= [], ("(", "[", "{"), (")", "]", "}") 
        for i in s:
            if i in l: 
                brackets.append(i)
            elif not brackets or l.index(brackets.pop())!= r.index(i): 
                return False
        return not brackets     