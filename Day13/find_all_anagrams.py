
class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        if len(p) > len(s):
            return []

        result = []
        p_count = {}
        window_count = {}

        for ch in p:
            p_count[ch] = p_count.get(ch, 0) + 1

        for i in range(len(p)):
            window_count[s[i]] = window_count.get(s[i], 0) + 1

        if window_count == p_count:
            result.append(0)

        for right in range(len(p), len(s)):
           
            new_char = s[right]
            window_count[new_char] = window_count.get(new_char, 0) + 1

          
            old_char = s[right - len(p)]
            window_count[old_char] -= 1

            if window_count[old_char] == 0:
                del window_count[old_char]

           
            if window_count == p_count:
                result.append(right - len(p) + 1)

        return result
