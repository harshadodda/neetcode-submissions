class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        unique = set()
        dup = False
        for num in nums:
            if not num in unique:
                unique.add(num)
            else:
                return True
        return dup