class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        unique_nums = list(set(nums))
        current_xor_set = {0}
        for _ in range(3):
            next_xor_set = set()
            for val in current_xor_set:
                for num in unique_nums:
                    next_xor_set.add(val ^ num)
            current_xor_set = next_xor_set
            
        return len(current_xor_set)