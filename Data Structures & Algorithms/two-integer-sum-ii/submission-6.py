class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # my first sol:
        # two pointer, increment slow when fast reaches end and reset fast to 1 + slow
        # slow, fast = 0, 1
        # while True:
        #     if numbers[slow] + numbers[fast] == target:
        #         return [slow + 1, fast + 1]
        #     if fast == len(numbers) - 1:
        #         slow += 1
        #         fast = slow + 1
        #     else:
        #         fast += 1
        # return False

        # optimal solution, o(n) time 
        slow, fast = 0, len(numbers) - 1

        while slow < fast:
            sum = numbers[slow] + numbers[fast]
            if sum > target:
                fast -= 1
            elif sum < target:
                slow += 1
            else:
                return [slow + 1, fast + 1]
