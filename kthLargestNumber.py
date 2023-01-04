class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        lis=[]
        lis = [int(i) for i in nums]
        lis.sort(reverse =True)
        return str(lis[k-1])