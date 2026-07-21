class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        extended = '1' + s + '1'
        segs = []
        curr_char = extended[0]
        curr_len = 0
        
        for char in extended:
            if char == curr_char:
                curr_len += 1
            else:
                segs.append((curr_char, curr_len))
                curr_char = char
                curr_len = 1
        segs.append((curr_char, curr_len))
        
        total_ones = s.count('1')
        max_delta = 0
        
        for idx in range(2, len(segs) - 1, 2):
            left_zeros = segs[idx - 1][1]
            right_zeros = segs[idx + 1][1]
            max_delta = max(max_delta, left_zeros + right_zeros)
            
        return total_ones + max_delta