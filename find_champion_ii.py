class Solution(object):
    def findChampion(self, n, edges):
        in_degree = [0] * n
        for u, v in edges:
            in_degree[v] += 1

        zero_in_degree = [node for node in range(n) if in_degree[node] == 0]

        if len(zero_in_degree) == 1:
            return zero_in_degree[0]
        else:
            return -1
# https://leetcode.com/problems/find-champion-ii
