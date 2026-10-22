def binary_search(nums, target):
    low = 0
    high = len(nums) - 1

    while low <= high:
        mid = low + (high - low) // 2

        if nums[mid] == target:
            return mid

        elif nums[mid] < target:
            low = mid + 1

        else:
            high = mid - 1

    return -1


nums = list(map(int, input("Enter sorted array: ").split()))
target = int(input("Enter target: "))

print("Index:", binary_search(nums, target))