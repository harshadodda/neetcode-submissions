class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        # // is the floor division operator to get whole number
        return nums[len(nums) // 2]