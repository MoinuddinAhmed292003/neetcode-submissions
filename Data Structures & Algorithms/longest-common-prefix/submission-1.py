class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        
        min_len = len(strs[0])
        for s in strs:
            if len(s) < min_len:
                min_len = len(s)

        pref = ""
        for i in range(min_len):
            char = strs[0][i]
            for j in range(1, len(strs)):
                if strs[j][i] != char:
                    return pref
            pref += char
        
        return pref