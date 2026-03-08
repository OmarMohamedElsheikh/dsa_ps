class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        current_sub = ""
        for c in s:
            if c in current_sub:
                ind = current_sub.index(c)
                current_sub = current_sub[ind+1:]
            current_sub += c
            longest = max(longest , len(current_sub))
        return longest        
