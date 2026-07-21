class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        t=sum(nums)
        ls=0
        for i,num in enumerate(nums):
            if ls==t-ls-num:
                return i
            ls+=num
        return -1