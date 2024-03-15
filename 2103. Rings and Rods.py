class Solution:
    def countPoints(self, rings: str) -> int:
        rods = []
        for i in range(10):
            rods.append("")

        for i in range(len(rings)):
            if rings[i].isalpha():
                rods[int(rings[i + 1])] += rings[i]
        
        count: int = 0
        for rod in rods:
            R = False
            B = False
            G = False
            if "R" in rod:
                R = True
            if "B" in rod:
                B = True
            if "G" in rod:
                G = True
            if R and B and G:
                count += 1
            
        return count
