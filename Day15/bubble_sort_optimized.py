
def bubble_sort_optimized(arr):
    n = len(arr)

    for i in range(n - 1):
        swapped = False

        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        # Stop if no swaps occurred
        if not swapped:
            break

    return arr


arr = [1, 2, 3, 4, 5]

print("Original array:", arr)
print("Sorted array:", bubble_sort_optimized(arr))
