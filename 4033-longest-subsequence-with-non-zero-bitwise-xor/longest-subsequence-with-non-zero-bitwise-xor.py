from typing import List

class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        # If there are no non-zero elements at all, it's impossible.
        if not any(nums):
            return 0
        
        # Calculate the XOR sum of the entire array
        xor_sum = 0
        for num in nums:
            xor_sum ^= num
            
        # If total XOR is non-zero, take the whole array
        if xor_sum != 0:
            return len(nums)
            
       
        return len(nums) - 1