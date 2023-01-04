class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        tot=0
        n=int((len(piles)/3))
        for i in range(n):
            me=piles[-(2+(i*2))]
            tot=tot+me
        return tot