class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cache = [-1] * len(cost)

        for i in range(len(cost)):
            if i == 0:
                cache[i] = cost[i]
            elif i == 1:
                cache[i] = cost[i]
            else:
                cache[i] = min(cache[i-2] + cost[i], cache[i-1] + cost[i])
        return min(cache[-1], cache[-2])
        