from collections import Counter

class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        n = len(s)
        counts = Counter(s)
        
        # Identify characters with odd frequencies
        odd_chars = [c for c, freq in counts.items() if freq % 2 != 0]
        
        # A palindrome can have at most one character with an odd frequency
        if len(odd_chars) > 1:
            return ""
        
        mid_char = odd_chars[0] if odd_chars else ""
        
        # Frequency of characters available for the first half of the palindrome
        half_counts = {c: freq // 2 for c, freq in counts.items()}
        
        half_n = n // 2
        best_pal = ""
        matched_prefix = []
        rem_counts = half_counts.copy()
        
        # Try to diverge from target at each possible index in the first half
        for idx in range(half_n + 1):
            if idx < half_n:
                cand_c = None
                # Find the smallest available character strictly greater than target[idx]
                for c_code in range(ord(target[idx]) + 1, ord('z') + 1):
                    c = chr(c_code)
                    if rem_counts.get(c, 0) > 0:
                        cand_c = c
                        break
                
                if cand_c:
                    cand_rem = rem_counts.copy()
                    cand_rem[cand_c] -= 1
                    
                    # Greedily fill the rest of the first half with the smallest available characters
                    suffix = []
                    for c_code in range(ord('a'), ord('z') + 1):
                        c = chr(c_code)
                        if cand_rem.get(c, 0) > 0:
                            suffix.append(c * cand_rem[c])
                    
                    cand_first = "".join(matched_prefix) + cand_c + "".join(suffix)
                    cand_pal = cand_first + mid_char + cand_first[::-1]
                    
                    if cand_pal > target:
                        if not best_pal or cand_pal < best_pal:
                            best_pal = cand_pal

            else:
                # Case where the entire first half perfectly matches target's first half
                cand_first = "".join(matched_prefix)
                cand_pal = cand_first + mid_char + cand_first[::-1]
                
                if cand_pal > target:
                    if not best_pal or cand_pal < best_pal:
                        best_pal = cand_pal
                        
            # Prepare for the next iteration: try to match target at the current index
            if idx < half_n:
                req_c = target[idx]
                if rem_counts.get(req_c, 0) > 0:
                    rem_counts[req_c] -= 1
                    matched_prefix.append(req_c)
                else:
                    # We don't have the required character to match target's prefix any further
                    break
                    
        return best_pal