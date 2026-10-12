def minSubArrayLen(target, nums):
    left = 0
    current_sum = 0
    min_length = len(nums) + 1

    right = 0
    while right < len(nums):
        current_sum += nums[right]

        while current_sum >= target:
            window_length = right - left + 1

            if window_length < minimum_length:
                min_length = window_length

            current_sum -= nums[left]
            left += 1

        right += 1

    if min_length == len(nums) + 1:
        return 0

    return minimum_length


print(minSubArrayLen(7, [2, 3, 1, 2, 4, 3]))