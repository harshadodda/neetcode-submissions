class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # calculate the sum of each duo
        # then see if the list has the number that with the duo adds to 0
        res = []
        nums.sort()

        for i, a in enumerate(nums):
            # if the prev value is the same as this one, continue, no dups
            if i > 0 and a == nums[i - 1]:
                continue

            l, r = i + 1, len(nums) - 1

            while l < r:
                target = a + nums[l] + nums[r]
                if target == 0:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
                elif target > 0: 
                    r -= 1
                else:
                    l += 1
            
        return res
            



            

