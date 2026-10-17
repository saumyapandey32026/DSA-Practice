class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        num_map = {}
        for i, num in enumerate(nums):
            cpt = target - num
            if cpt in num_map:
                return [num_map[cpt], i]
            num_map[num] = i
