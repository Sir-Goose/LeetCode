class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        can = capacity
        steps = 0
        plant_status = [False] * len(plants)
        pos = -1
        while pos < len(plants) -1:
            pos += 1
            steps += 1
            if plant_status[pos] == False:
                if can - plants[pos] >= 0:
                    can -= plants[pos]
                    plant_status[pos] = True
                else:
                    steps += pos -1
                    pos = -1
                    can = capacity
        return steps
