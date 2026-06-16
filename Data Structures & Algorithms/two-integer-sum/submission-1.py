class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hm = {}
        for index, num in enumerate(nums):
            if num not in hm:
                hm[num] = [target - num, index]
            if target - num in hm and index != hm[target - num][1]:
                return [hm[target - num][1], index]
        return []

        