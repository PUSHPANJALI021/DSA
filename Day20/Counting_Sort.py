def counting_sort(arr):
    if len(arr) == 0:
        return arr

    maximum = arr[0]
    minimum = arr[0]

    for num in arr:
        if num > maximum:
            maximum = num
        if num < minimum:
            minimum = num

    count = [0] * (maximum - minimum + 1)

    for num in arr:
        count[num - minimum] += 1

    index = 0

    for i in range(len(count)):
        while count[i] > 0:
            arr[index] = i + minimum
            index += 1
            count[i] -= 1

    return arr


arr = list(map(int, input("Enter array elements: ").split()))
print("Sorted array:", counting_sort(arr))