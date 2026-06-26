class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) < len(nums)

        # # sol 2:
        # hashset = set()

        # for num in nums:
        #     if n in hashset:
        #         return true
        #     hashset.add(num)
        