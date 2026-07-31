class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # sort the list
        # fix first num, 2 sum on the rest of the array to find
        # what = 0 with fixed num
        # skip i if its same, no dups
        res = []
        nums.sort()

        for i, val in enumerate(nums):
            # if the prev value is the same as this one, continue, no dups
            if i > 0 and val == nums[i - 1]:
                continue

            l, r = i + 1, len(nums) - 1

            # after we set the first value to nums[i], do two sum on the rest of 
            # the values to equal 0
            while l < r:
                target = val + nums[l] + nums[r]
                if target == 0:
                    res.append([val, nums[l], nums[r]])
                    l += 1 
                    # if we have same num, skip it, no dups
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
                elif target > 0: 
                    r -= 1
                else:
                    l += 1
            
        return res
            



            

