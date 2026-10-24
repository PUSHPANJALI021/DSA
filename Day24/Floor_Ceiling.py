def find_floor(nums, target):
    low = 0
    high = len(nums) - 1
    answer = -1

    while low <= high:
        mid = low + (high - low) // 2

        if nums[mid] <= target:
            answer = nums[mid]
            low = mid + 1
        else:
            high = mid - 1

    return answer


def find_ceiling(nums, target):
    low = 0
    high = len(nums) - 1
    answer = -1

    while low <= high:
        mid = low + (high - low) // 2

        if nums[mid] >= target:
            answer = nums[mid]
            high = mid - 1
        else:
            low = mid + 1

    return answer


nums = list(map(int, input("Enter sorted array: ").split()))
target = int(input("Enter target: "))

print("Floor:", find_floor(nums, target))
print("Ceiling:", find_ceiling(nums, target))