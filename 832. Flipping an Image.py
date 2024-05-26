class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for j in range(len(image)):
            new_row = []
            for i in range(len(image[j]) - 1, -1, -1):
                new_row.append(image[j][i])
            image[j] = new_row
       
        for i in range(len(image)):
            for k in range(len(image[i])):
                if image[i][k] == 1:
                    image[i][k] = 0
                elif image[i][k] == 0:
                    image[i][k] = 1
       
        return image

