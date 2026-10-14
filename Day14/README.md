Window + Condition Tracking

1. Max Consecutive Ones III

Approach: Use a sliding window and track zeros. Shrink the window when zeros exceed k.

Time Complexity: O(n)

Space Complexity: O(1)

2. Longest Repeating Character Replacement

Approach: Maintain character frequencies and track maximum frequency. Shrink the window when replacements exceed k.

Time Complexity: O(n)

Space Complexity: O(1) for a fixed alphabet

3. Longest Substring Without Repeating Characters

Approach: Use a sliding window and dictionary to track characters. Shrink the window when a duplicate appears.

Time Complexity: O(n) average

Space Complexity: O(min(n, alphabet size))