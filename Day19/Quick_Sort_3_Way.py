
def quick_sort_3way(arr, low, high):
    if low >= high:
        return

    pivot = arr[low]
    lt = low
    mid = low
    gt = high

    while mid <= gt:
        if arr[mid] < pivot:
            arr[lt], arr[mid] = arr[mid], arr[lt]
            lt += 1
            mid += 1

        elif arr[mid] > pivot:
            arr[mid], arr[gt] = arr[gt], arr[mid]
            gt -= 1

        else:
            mid += 1

    quick_sort_3way(arr, low, lt - 1)
    quick_sort_3way(arr, gt + 1, high)


arr = [4, 2, 4, 1, 4, 3, 2, 4]
quick_sort_3way(arr, 0, len(arr) - 1)
print(arr)
