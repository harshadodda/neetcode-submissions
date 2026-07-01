class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # set to delete dups
        # find nums who are start of seq, then find length of that seq 
        # update longest as we go
        nums_set = set(nums)
        longest = 0
        start_seq = []
        for num in nums:
            if num - 1 not in nums_set:
                length = 0
                while num + length in nums_set:
                    length += 1
                longest = max(length, longest)
        return longest

             
        