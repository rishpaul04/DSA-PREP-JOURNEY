from collections import deque
from typing import List

class Solution:
    def findMaxPathScore(self, edges: List[List[int]], online: List[bool], k: int) -> int:
        n = len(online)
        
        # Extract and sort unique edge costs for binary search
        unique_costs = sorted(list(set(edge[2] for edge in edges)))
        
        # Pre-build adjacency representation for faster access
        # Filtering out edges that touch offline nodes immediately
        valid_edges = []
        for u, v, cost in edges:
            if online[u] and online[v]:
                valid_edges.append((u, v, cost))
                
        def can_reach_with_min_cost(min_edge_threshold: int) -> bool:
            # dp[i] stores the minimum path recovery cost from node 0 to node i
            dp = [float('inf')] * n
            dp[0] = 0
            
            # Build graph dynamically for edges >= min_edge_threshold
            adj = [[] for _ in range(n)]
            in_degree = [0] * n
            
            for u, v, cost in valid_edges:
                if cost >= min_edge_threshold:
                    adj[u].append((v, cost))
                    in_degree[v] += 1
            
            # Topological Sort using Kahn's algorithm
            queue = deque([i for i in range(n) if in_degree[i] == 0])
            
            while queue:
                u = queue.popleft()
                current_cost = dp[u]
                
                for v, cost in adj[u]:
                    if current_cost + cost < dp[v]:
                        dp[v] = current_cost + cost
                    in_degree[v] -= 1
                    if in_degree[v] == 0:
                        queue.append(v)
            
            return dp[n - 1] <= k

        # Binary search over the indices of unique_costs
        low = 0
        high = len(unique_costs) - 1
        ans = -1
        
        while low <= high:
            mid = (low + high) // 2
            threshold = unique_costs[mid]
            
            if can_reach_with_min_cost(threshold):
                ans = threshold  # Found a valid lower-bound bottleneck; try a larger one
                low = mid + 1
            else:
                high = mid - 1
                
        return ans
