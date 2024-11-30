from collections import defaultdict, deque

class Solution(object):
    def validArrangement(self, pairs):
        # Step 1: Build graph and track in-degrees and out-degrees
        graph = defaultdict(deque)
        in_degree = defaultdict(int)
        out_degree = defaultdict(int)
        
        for start, end in pairs:
            graph[start].append(end)
            out_degree[start] += 1
            in_degree[end] += 1
        
        # Step 2: Find the starting node for Eulerian path
        start_node = pairs[0][0]
        for node in graph:
            if out_degree[node] - in_degree[node] == 1:
                start_node = node
                break

        # Step 3: Hierholzer's algorithm to find Eulerian path
        stack = [start_node]
        path = []
        
        while stack:
            while graph[stack[-1]]:
                next_node = graph[stack[-1]].popleft()
                stack.append(next_node)
            path.append(stack.pop())
        
        # Step 4: Reverse path and construct result
        path.reverse()
        result = [[path[i], path[i + 1]] for i in range(len(path) - 1)]
        return result
