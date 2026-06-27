class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # my solution, selection sort 0(n^2)
        # i = 0
        # j = i + 1
        # while i < len(nums):
        #     while j < len(nums):
        #         if nums[i] > nums[j]:
        #             nums[i], nums[j] = nums[j], nums[i] # python lets you swap nums without temp
        #         j += 1
        #     i += 1
        #     j = i + 1

        i, left, right = 0, 0, len(nums) - 1

        while i <= right:
            if nums[i] == 0:
                nums[left], nums[i] = nums[i], nums[left]
                left += 1
            elif nums[i] == 2:
                nums[right], nums[i] = nums[i], nums[right]
                right -= 1
                i -= 1
            i += 1
        

