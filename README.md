Sliding Window + HashMap

Problem

1. Contains Duplicate II

Goal: Determine whether the array contains two equal elements whose indices differ by at most k.

Approach:

Use a hashmap to store the most recent index of each number.

Check the distance between the current index and the stored index.

Return True if the distance is at most k; otherwise, update the index.

Time Complexity: O(n)
Space Complexity: O(n)

2. Find All Anagrams in a String

Goal: Find all starting indices of substrings of s that are anagrams of p.

Approach:

Count the character frequencies in p.

Maintain a sliding window of size len(p) in s.

Add the incoming character and remove the outgoing character.

Compare the frequency maps and store matching starting indices.

Time Complexity: O(n × Σ) in the worst case, where Σ is the character set size.
Space Complexity: O(Σ)

3. Permutation in String

Goal: Check whether s2 contains any substring that is a permutation of s1.

Approach:

Build a character-frequency map for s1.

Maintain a fixed-size sliding window in s2.

Update the frequency map as the window moves.

Return True if any window has the same character frequencies.

Time Complexity: O(n × Σ) in the worst case.
Space Complexity: O(Σ)