from operator import indexOf


class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if target < nums[0]:
            return 0
        if target > nums[-1]:
            return len(nums)
        
        for i in range(len(nums)):
            print(i)
            if nums[i] == target:
                return i
            elif nums[i-1] < target and nums[i] > target:
                return i
            

obj = Solution()
            
nums = [1,3,5,6]
target = 4

obj = Solution()


print(obj.searchInsert(nums,target))