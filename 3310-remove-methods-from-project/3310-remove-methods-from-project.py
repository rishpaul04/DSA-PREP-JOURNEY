from collections import deque
from typing import List

class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        # Step 1: Build the adjacency list for the directed graph
        adj = [[] for _ in range(n)]
        for u, v in invocations:
            adj[u].append(v)
            
        # Step 2: Find all suspicious methods using BFS
        suspicious = set([k])
        queue = deque([k])
        
        while queue:
            curr = queue.popleft()
            for neighbor in adj[curr]:
                if neighbor not in suspicious:
                    suspicious.add(neighbor)
                    queue.append(neighbor)
                    
        # Step 3: Check if any non-suspicious method invokes a suspicious method
        can_remove = True
        for u, v in invocations:
            if u not in suspicious and v in suspicious:
                can_remove = False
                break
                
        # Step 4: Return the remaining methods
        if can_remove:
            return [i for i in range(n) if i not in suspicious]
        else:
            return list(range(n))