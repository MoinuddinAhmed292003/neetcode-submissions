class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        d = {}

        for i in s:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        
        d1 = {}

        for i in t:
            if i in d1:
                d1[i] += 1
            else:
                d1[i] = 1
        
        return d == d1
        
