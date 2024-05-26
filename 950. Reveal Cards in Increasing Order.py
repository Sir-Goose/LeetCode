class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        n = len(deck)
        ans = [0] * n
        deck.sort()
        q = collections.deque(range(n))
        j = 0
        while q:
            i = q.popleft()
            ans[i] = deck[j]
            j += 1
            if q:
                q.append(q.popleft())
        return ans

