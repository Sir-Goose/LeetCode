class Solution:
    def processQueries(self, queries: List[int], m: int) -> List[int]:
        output = []
        
        P = [0] * m
        for i in range(m):
            P[i] = i + 1
        print(P)

        for query in queries:
            output.append(P.index(query))
            P = [P.pop(P.index(query))] + P
        
        return output



