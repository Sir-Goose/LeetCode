class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles = sorted(piles, reverse=True)
        n = int(len(piles) / 3)
        print(n)
        max_coins = 0
        print(piles)

        optimal_list = []
        while(piles):
            optimal_list.append(piles.pop(0))
            optimal_list.append(piles.pop(0))
            optimal_list.append(piles.pop())


        for i in range(2, len(optimal_list), 3):
            print(i - 1)
            max_coins += optimal_list[i - 1]
            print(optimal_list[i - 1])
            

        return max_coins

