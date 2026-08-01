class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        longest = 0
        charSet = set()

        # go through the whole string
        for r in range(len(s)):
            while s[r] in charSet:
                # move left pointer while right pointer is dup letter
                charSet.remove(s[l])
                l += 1
            # add right letter when its not dup
            charSet.add(s[r])
            # calculate window every time
            longest = max(longest, r - l + 1)
        return longest
