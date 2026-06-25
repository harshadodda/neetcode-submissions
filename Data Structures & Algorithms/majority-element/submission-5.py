class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # sol 1: 
        res, count = 0, 0
        
        for n in nums:
            # if count is 0, means this num and another num have the same # of occurances
            if count == 0:
                # change num to new num
                res = n 
            # if the number is the same as res, increment by 1, and otherwise, subtract 1
            count +=  (1 if n == res else -1)
        return res

        # sol 2:
        # nums.sort()
        # # // is the floor division operator to get whole number
        # return nums[len(nums) // 2]