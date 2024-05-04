class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        pos_a = edges[0][0]
        pos_b = edges[0][1]

        for edge in edges:
            if pos_a not in edge:
                pos_a = None
            if pos_b not in edge:
                pos_b = None
        
        if pos_a:
            return pos_a
        else:
            return pos_b
            
