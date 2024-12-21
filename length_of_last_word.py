class Solution(object):
    def lengthOfLastWord(self, s):
        # Strip trailing spaces and split the string into words
        words = s.strip().split()
        # Return the length of the last word
        return len(words[-1]) 