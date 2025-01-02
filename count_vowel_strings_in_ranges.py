class Solution(object):
    def vowelStrings(self, words, queries):
        vowels = {'a', 'e', 'i', 'o', 'u'}

        # Precompute a prefix sum array for the number of valid strings
        n = len(words)
        prefix = [0] * (n + 1)

        for i in range(n):
            if words[i][0] in vowels and words[i][-1] in vowels:
                prefix[i + 1] = prefix[i] + 1
            else:
                prefix[i + 1] = prefix[i]

        # Answer each query using the prefix sum array
        result = []
        for li, ri in queries:
            result.append(prefix[ri + 1] - prefix[li])

        return result
