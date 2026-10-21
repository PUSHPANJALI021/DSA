def frequency_sort(nums):
    freq = {}

    for num in nums:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1

    # Manual insertion sort
    for i in range(1, len(nums)):
        key = nums[i]
        j = i - 1

        while j >= 0:
            if freq[nums[j]] > freq[key]:
                nums[j + 1] = nums[j]

            elif freq[nums[j]] == freq[key] and nums[j] < key:
                nums[j + 1] = nums[j]

            else:
                break

            j -= 1

        nums[j + 1] = key

    return nums


nums = list(map(int, input("Enter elements: ").split()))
print("Frequency sorted array:", frequency_sort(nums))