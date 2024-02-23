class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:

        collection_time: int = 0
        travel_time: int = 0
        num_trucks: int = 0

        for i in range(len(garbage)):
            collection_time += len(garbage[i])
            num_trucks = max(num_trucks, len(garbage))

        
        # find the last house truck had to get to
        last_house_metal: int = 0
        last_house_paper: int = 0
        last_house_glass: int = 0
        for i in range(len(garbage)):
            if i == 0:
                continue
            
            if "G" in garbage[i]:
                last_house_glass = i 
            if "P" in garbage[i]:
                last_house_paper = i 

            if "M" in garbage[i]:
                last_house_metal = i 

        metal_travel_time: int = 0
        paper_travel_time: int = 0
        glass_travel_time: int = 0
        
        print(last_house_metal)
        print(last_house_paper)
        for i in range(last_house_metal):
            metal_travel_time += travel[i]

        for i in range(last_house_paper):
            paper_travel_time += travel[i]

        for i in range(last_house_glass):
            glass_travel_time += travel[i]

        total_travel_time: int = metal_travel_time + paper_travel_time + glass_travel_time + collection_time

        return total_travel_time
        
