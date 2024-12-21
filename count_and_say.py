class Solution(object):
    def countAndSay(self, n):
        def run_length_encode(s):
            """
            Helper function to compute the RLE of a string.
            """
            encoded = []
            i = 0
            while i < len(s):
                count = 1
                # Count consecutive characters
                while i + 1 < len(s) and s[i] == s[i + 1]:
                    i += 1
                    count += 1
                # Append the count and the character
                encoded.append(str(count) + s[i])
                i += 1
            return ''.join(encoded)
        
        # Base case: countAndSay(1) = "1"
        result = "1"
        
        # Iteratively compute countAndSay(n)
        for _ in range(1, n):
            result = run_length_encode(result)
        
        return result
