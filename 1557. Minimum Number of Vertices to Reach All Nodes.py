class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        reachable = set(edge[1] for edge in edges)
        return [node for node in range(n) if node not in reachable]
        
