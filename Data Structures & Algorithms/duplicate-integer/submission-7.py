class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #return len(set(nums)) < len(nums)

        # sol 2:
        hashset = set()

        for num in nums:
            if num in hashset:
                return True
            hashset.add(num)
        return False