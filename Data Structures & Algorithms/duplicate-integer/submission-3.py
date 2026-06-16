class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        set_container = set()
        dup = False
        for num in nums:
            if not num in set_container:
                set_container.add(num)
            else:
                return True
        return dup