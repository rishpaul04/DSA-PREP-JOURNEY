from collections import deque
from typing import List

class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        # Step 1: Build the adjacency list
        graph = {i: [] for i in range(1, n + 1)}
        for u, v, w in roads:
            graph[u].append((v, w))
            graph[v].append((u, w))
        
        # Step 2: BFS initialization
        queue = deque([1])
        visited = {1}
        min_score = float('inf')
        
        # Step 3: Traverse the component containing city 1
        while queue:
            node = queue.popleft()
            
            for neighbor, weight in graph[node]:
                # Update the minimum score for every road seen in this component
                min_score = min(min_score, weight)
                
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
                    
        return min_score