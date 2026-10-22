class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
# SELECTION SORT =>
        # for i in range(0,len(nums)-1):
        #     min_idx = i
        #     for j in range(i+1,len(nums)):
        #         if nums[min_idx] > nums[j]:
        #             min_idx = j 
        #     nums[i], nums[min_idx] = nums[min_idx], nums[i]  

        # return nums

      
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
        # for i in range(len(nums)):
        #     j = i
        #     while(j>0 and nums[j-1]>nums[j]):
        #         nums[j-1], nums[j] = nums[j], nums[j-1]
        #         j -= 1
        # return nums
        
# MERGE SORT =>  
        def mergeSort(nums,low,high):
            mid = (low+high)//2

            if low >= high:
                return
            else:
                mergeSort(nums, low, mid)
                mergeSort(nums, mid+1, high)

                merge(nums,low,mid,high)

        def merge(nums,low,mid,high):
            temp = []
            left = low
            right = mid+1

            while(left<=mid and right<=high):
                if nums[left] <= nums[right]:
                    temp.append(nums[left])
                    left += 1
                else:
                    temp.append(nums[right])
                    right += 1
            while(left <= mid):
                temp.append(nums[left])
                left += 1
            while(right <= high):
                temp.append(nums[right])
                right += 1
            # for i in range(len(nums)):
            #     nums[i] = temp[i]
            # return nums
            for i in range(len(temp)):
                nums[low+i] = temp[i]

        mergeSort(nums, 0, len(nums) - 1)
        return nums






























