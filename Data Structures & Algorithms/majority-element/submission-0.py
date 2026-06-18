class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        sorted(nums)
        # // is the floor division operator to get whole number
        if nums[len(nums) // 2] == nums[len(nums) - 1]:
            return nums[len(nums) - 1]
        else:
            return nums[0]