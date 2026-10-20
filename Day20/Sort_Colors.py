def sort_binary_array(arr):
    count_zero = 0

    for num in arr:
        if num == 0:
            count_zero += 1

    for i in range(len(arr)):
        if i < count_zero:
            arr[i] = 0
        else:
            arr[i] = 1

    return arr


arr = list(map(int, input("Enter array elements (0 and 1): ").split()))
print("Sorted array:", sort_binary_array(arr))