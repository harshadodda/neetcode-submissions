class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0 # write all non val numbers to front of list
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1 # move through list to migrate all valid numbers to front
        return k # k ends up being the number of elements that arent val