 DSA Practice — Day 12
 1. Minimum Size Subarray Sum

Problem: Find the minimum length of a contiguous subarray whose sum is greater than or equal to the target. Return `0` if no such subarray exists.

 Approach
- Use the sliding window technique with two pointers, `left` and `right`.
- Expand the window by adding elements. When the sum reaches the target, update the minimum length and shrink the window from the left.

Complexity
- Time:`O(n)` — Each element enters and leaves the window at most once.
- Space: `O(1)` — Only a constant number of variables are used.


 2. Longest Subarray with Sum K

Problem: Find the maximum length of a contiguous subarray whose sum is exactly `k`. The array may contain positive, zero, and negative numbers.

Approach
- Use prefix sum and a dictionary to store the earliest index of each prefix sum.
- Check whether `prefix_sum - k` exists in the dictionary. If it does, calculate the subarray length and update the maximum length.

 Complexity
- Time: `O(n)` average — The array is traversed once, with average constant-time dictionary operations.
- Space: `O(n)` — The dictionary can store up to `n` distinct prefix sums.



3. Fruit Into Baskets

Problem: Find the maximum number of fruits that can be collected from a contiguous sequence of trees containing at most two fruit types.

 Approach
- Use a sliding window and a dictionary to count each fruit type in the current window.
- When more than two types appear, shrink the window from the left until only two types remain. Track the maximum window length.

 Complexity
- Time: `O(n)` — Each tree is added once, and the left pointer moves forward at most `n` times.
- Space:`O(1)` — The dictionary size stays bounded because the window is reduced whenever more than two fruit types appear.


 Summary

| Problem | Time Complexity | Space Complexity |
|---|---|---|
| Minimum Size Subarray Sum | `O(n)` | `O(1)` |
| Longest Subarray with Sum K | `O(n)`
| `O(n)` |
| Fruit Into Baskets | `O(n)` | `O(1)` |

