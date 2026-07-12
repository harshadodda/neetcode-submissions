class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        slow, fast = 0, 1
        while True:
            if numbers[slow] + numbers[fast] == target:
                return [slow + 1, fast + 1]
            if fast == len(numbers) - 1:
                slow += 1
                fast = slow + 1
            else:
                fast += 1
        return False
