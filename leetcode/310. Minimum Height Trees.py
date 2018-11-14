class Solution:
    def findMinHeightTrees(self, n, edges):
        """

        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        if n <= 1:
            return [0]
        degrees = [0] * n
        graph = {x: [] for x in range(n)}
        for p in edges:
            degrees[p[1]] += 1
            degrees[p[0]] += 1
            graph[p[1]].append(p[0])
            graph[p[0]].append(p[1])

        queue = [x for x in range(0, n) if degrees[x] == 1]
        ret = []
        while queue:
            temp = []
            ret = queue[:]
            for x in queue:
                for n in graph[x]:
                    degrees[n] -= 1
                    if degrees[n] == 1:
                        temp.append(n)
            queue = temp

        return ret


if __name__ == '__main__':
    sl = Solution()
    ret = sl.findMinHeightTrees(6,
[[0,1],[0,2],[0,3],[3,4],[4,5]])
    print(ret)