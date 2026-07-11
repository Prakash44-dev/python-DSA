from typing import List

class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = [[] for _ in range(n)]

        # Build adjacency list
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = [False] * n

        def dfs(node):
            visited[node] = True
            nodes = 1
            degree_sum = len(graph[node])

            for nei in graph[node]:
                if not visited[nei]:
                    child_nodes, child_degrees = dfs(nei)
                    nodes += child_nodes
                    degree_sum += child_degrees

            return nodes, degree_sum

        ans = 0

        for i in range(n):
            if not visited[i]:
                nodes, degree_sum = dfs(i)

                # Every edge is counted twice in degree_sum
                edge_count = degree_sum // 2

                # Complete graph with k nodes has k*(k-1)/2 edges
                if edge_count == nodes * (nodes - 1) // 2:
                    ans += 1

        return ans