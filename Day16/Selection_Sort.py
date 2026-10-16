def find_k_smallest(arr, k):
    n = len(arr)

    if k < 0 or k > n:
        return []

    for i in range(k):
        smallest = i

        for j in range(i + 1, n):
            if arr[j] < arr[smallest]:
                smallest = j

        temp = arr[i]
        arr[i] = arr[smallest]
        arr[smallest] = temp

    result = []

    for i in range(k):
        result.append(arr[i])

    return result


arr = [12, 3, 5, 7, 19, 1]
k = 3

print(find_k_smallest(arr, k))