class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        path_count = [True for value in range(len(paths))]


        for j in range(len(paths)):
            curr = paths[j][1]
            for i in range(len(paths)):
                if curr == paths[i][0]:
                    path_count[j] = False
                    
                
        for i in range(len(path_count)):
            if path_count[i] == True:
                return paths[i][1]

