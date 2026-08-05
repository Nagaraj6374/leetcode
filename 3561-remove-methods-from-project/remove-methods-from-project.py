from typing import List

class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        # Step 1: Build adjacency list for direct invocations (a -> b)
        adj = [[] for _ in range(n)]
        for u, v in invocations:
            adj[u].append(v)
            
        # Step 2: Find all suspicious methods using BFS starting from method k
        suspicious = set()
        queue = [k]
        suspicious.add(k)
        
        while queue:
            curr = queue.pop(0)
            for neighbor in adj[curr]:
                if neighbor not in suspicious:
                    suspicious.add(neighbor)
                    queue.append(neighbor)
                    
        # Step 3: Check if any non-suspicious method invokes a suspicious method
        for u, v in invocations:
            if u not in suspicious and v in suspicious:
                # Removal condition fails; return all methods
                return list(range(n))
                
        # Step 4: If no external invocations exist, return only non-suspicious methods
        return [i for i in range(n) if i not in suspicious]