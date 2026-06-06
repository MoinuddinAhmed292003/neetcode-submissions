class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d = {}
        maj = len(nums) / 2

        for i  in nums:
            if i not in d:
                d[i] = 1
            else:
                d[i] += 1
        
        for k, v in d.items():
            if v >= maj:
                return k
        
