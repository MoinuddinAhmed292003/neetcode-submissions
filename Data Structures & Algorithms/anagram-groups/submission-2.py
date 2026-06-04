class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = {}

        for s in strs:

            soort = ''.join(sorted(s))

            if soort not in group:
                group[soort] = []

            group[soort].append(s)

        return list(group.values())

