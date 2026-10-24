def search_range(nums, target):
    first = -1
    last = -1

    # Find first occurrence
    low = 0
    high = len(nums) - 1

    while low <= high:
        mid = low + (high - low) // 2

        if nums[mid] == target:
            first = mid
            high = mid - 1
        elif nums[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    # Find last occurrence
    low = 0
    high = len(nums) - 1

    while low <= high:
        mid = low + (high - low) // 2

        if nums[mid] == target:
            last = mid
            low = mid + 1
        elif nums[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return [first, last]


nums = list(map(int, input("Enter sorted array: ").split()))
target = int(input("Enter target: "))

print(search_range(nums, target))