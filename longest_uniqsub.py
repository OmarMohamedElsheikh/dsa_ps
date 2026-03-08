class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        char_ind = {}
        start = 0 
        for i, c in enumerate(s):
            if c in char_ind and char_ind[c] >= start:
                start = char_ind[c] +1
            char_ind[c] = i
            longest = max(longest , i - start + 1)
        return longest
