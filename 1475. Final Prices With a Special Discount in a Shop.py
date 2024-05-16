class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        answer = []
        for i in range(len(prices)):
            discount = 1001
            for j in range(i + 1, len(prices)):
                if prices[j] <= prices[i] and prices[j] < discount:
                    discount = prices[j]
                    break
            
            if discount != 1001:
                answer.append(prices[i] - discount)
            else:
                answer.append(prices[i])
        return answer

