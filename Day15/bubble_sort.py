
def bubble_sort(arr):
    n = len(arr)

    for i in range(n - 1):
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr


arr = [5, 1, 4, 2, 8]

print("Original array:", arr)
print("Sorted array:", bubble_sort(arr))
