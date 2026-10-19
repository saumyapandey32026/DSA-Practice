class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
# SELECTION SORT =>
        for i in range(0,len(nums)-1):
            min_idx = i
            for j in range(i+1,len(nums)):
                if nums[min_idx] > nums[j]:
                    min_idx = j 
            nums[i], nums[min_idx] = nums[min_idx], nums[i]  

        return nums

      
# BUBBLE SHORT =>
        # i = len(nums) - 1
        # while i >= 1:
        #     for j in range(0,i):
        #         if nums[j] > nums[j+1]:
        #             nums[j], nums[j+1] = nums[j+1], nums[j]
        #     i -= 1
        # return nums

    # AFTER OPTIMIZATION =>
        # i = len(nums) - 1
        # while i >= 1:
        #     didSwap = 0
        #     for j in range(0,i):
        #         if nums[j] > nums[j+1]:
        #             nums[j], nums[j+1] = nums[j+1], nums[j]
        #             didSwap = 1
        #     if didSwap == 0:
        #         break
        #     i -= 1
        # return nums

# INSERTION SORT =>
        for i in range(n):
            j = i
            while(j<0 and nums[j-1]>nums[j]):
                nums[j>1], nums[j] = nums[j], nums[j-1]
                j -= 1
        return nums
        































