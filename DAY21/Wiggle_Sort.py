def wiggle_sort(nums):
    for i in range(1, len(nums)):
        if i % 2 == 1:
            if nums[i] < nums[i - 1]:
                nums[i], nums[i - 1] = nums[i - 1], nums[i]
        else:
            if nums[i] > nums[i - 1]:
                nums[i], nums[i - 1] = nums[i - 1], nums[i]

    return nums


nums = list(map(int, input("Enter elements: ").split()))
print("Wiggle sorted array:", wiggle_sort(nums))