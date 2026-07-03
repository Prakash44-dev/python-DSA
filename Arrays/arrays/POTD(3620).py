from typing import List
from collections import deque

class Solution:
    def findMaxPathScore(self, edges: List[List[int]], online: List[bool], k: int) -> int:
        n = len(online)

        max_cost = 0
        for _, _, w in edges:
            max_cost = max(max_cost, w)

        def check(limit):
            graph = [[] for _ in range(n)]
            indegree = [0] * n

            for u, v, w in edges:
                if w < limit:
                    continue
                if u != 0 and u != n - 1 and not online[u]:
                    continue
                if v != 0 and v != n - 1 and not online[v]:
                    continue

                graph[u].append((v, w))
                indegree[v] += 1

            q = deque()
            for i in range(n):
                if indegree[i] == 0:
                    q.append(i)

            INF = float("inf")
            dist = [INF] * n
            dist[0] = 0

            while q:
                u = q.popleft()

                if dist[u] != INF:
                    for v, w in graph[u]:
                        if dist[v] > dist[u] + w:
                            dist[v] = dist[u] + w

                for v, _ in graph[u]:
                    indegree[v] -= 1
                    if indegree[v] == 0:
                        q.append(v)

            return dist[n - 1] <= k

        if not check(0):
            return -1

        left, right = 0, max_cost
        ans = 0

        while left <= right:
            mid = (left + right) // 2
            if check(mid):
                ans = mid
                left = mid + 1
            else:
                right = mid - 1

        return ans