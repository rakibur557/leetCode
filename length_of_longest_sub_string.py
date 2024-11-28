class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Dictionary to store the last index of each character
        char_index = {}
        max_length = 0
        start = 0  # Start of the current window

        for end, char in enumerate(s):
            # If the character is already in the substring, move the start to the right
            if char in char_index and char_index[char] >= start:
                start = char_index[char] + 1
            
            # Update the character's index
            char_index[char] = end
            
            # Update the maximum length of the substring
            max_length = max(max_length, end - start + 1)

        return max_length
# https://leetcode.com/problems/longest-substring-without-repeating-characters
