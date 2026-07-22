class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        c=sum(nums[:k])
        max=c
        for i in range(k,len(nums)):
            c+=nums[i]-nums[i-k]
            if c>max:
                max=c
        return max/k