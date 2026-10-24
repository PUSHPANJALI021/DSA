def count_occurrences(nums, target):
    first = -1
    last = -1

    # Find first occurrence
    low = 0
    high = len(nums) - 1

    while low <= high:
        mid = low + (high - low) // 2

        if nums[mid] >= target:
            if nums[mid] == target:
                first = mid
            high = mid - 1
        else:
            low = mid + 1

    # Find last occurrence
    low = 0
    high = len(nums) - 1

    while low <= high:
        mid = low + (high - low) // 2

        if nums[mid] <= target:
            if nums[mid] == target:
                last = mid
            low = mid + 1
        else:
            high = mid - 1

    if first == -1:
        return 0

    return last - first + 1


nums = list(map(int, input("Enter sorted array: ").split()))
target = int(input("Enter target: "))

print("Occurrences:", count_occurrences(nums, target))