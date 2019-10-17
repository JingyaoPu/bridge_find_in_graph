from collections import defaultdict


class Solution:
    def bridge(self, n, edges):
        res = []
        G = defaultdict(list)
        for u,v in edges:
            G[u].append(v)
            G[v].append(u)

        visited = [False]*(n+1)
        parent = [-1]*(n+1)
        minTimes = [float('inf')]*(n+1)
        self.time = 0

        def traverse(v):
            if visited[v]:
                return
            visited[v] = True
            time = self.time
            minTimes[v] = self.time
            self.time += 1
            for v2 in G[v]:
                if parent[v] == v2:
                    continue
                parent[v2] = v
                traverse(v2)
                if minTimes[v2] > time:
                    res.append((v, v2))
                else:
                    minTimes[v] = min(minTimes[v2],minTimes[v])

        for i in range(1,n+1):
            traverse(i)
        return res



sol = Solution()
print (sol.bridge(5,[[1, 2], [1, 3], [3, 4], [1, 4], [4, 5]]))