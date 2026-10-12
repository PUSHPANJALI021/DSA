nums = [1, -1, 5, -2, 3]
k = 3

prefix_sum = 0
max_length = 0
prefix_index = {0: -1}

for i in range(len(nums)):
    prefix_sum += nums[i]

    needed = prefix_sum - k

    if needed in prefix_index:
        length = i - prefix_index[needed]

        if length > max_length:
            max_length = length

    if prefix_sum not in prefix_index:
        prefix_index[prefix_sum] = i

print("Maximum length:", max_length)