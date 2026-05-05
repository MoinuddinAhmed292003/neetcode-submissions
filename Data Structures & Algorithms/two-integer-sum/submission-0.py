class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}

        for i in range(len(nums)):
            diff = target - nums[i]
            if nums[i] in d:
                return [nums.index(diff), i]
            else:
                d[diff] = 1
