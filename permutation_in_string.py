
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1_count = {}
        window_count = {}

        for ch in s1:
            s1_count[ch] = s1_count.get(ch, 0) + 1

        for i in range(len(s1)):
            window_count[s2[i]] = window_count.get(s2[i], 0) + 1

        if s1_count == window_count:
            return True

        for right in range(len(s1), len(s2)):
           
            new_char = s2[right]
            window_count[new_char] = window_count.get(new_char, 0) + 1

            
            old_char = s2[right - len(s1)]
            window_count[old_char] -= 1

            if window_count[old_char] == 0:
                del window_count[old_char]

            if s1_count == window_count:
                return True

        return False
