# Question 1: Selection Sort

def selection_sort(arr):
    n = len(arr)

    for i in range(n):
        min_index = i

        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr


arr = [64, 25, 12, 22, 11]
print(selection_sort(arr))


# Question 2: Find K Smallest Elements

def k_smallest(arr, k):
    n = len(arr)

    if k < 0 or k > n:
        return []

    for i in range(k):
        min_index = i

        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr[:k]


arr = [7, 10, 4, 3, 20, 15]
k = 3
print(k_smallest(arr, k))


# Question 3: Sort Characters By Frequency

def frequency_sort(s):
    freq = {}

    for ch in s:
        if ch in freq:
            freq[ch] += 1
        else:
            freq[ch] = 1

    chars = []

    for ch in s:
        if ch not in chars:
            chars.append(ch)

    n = len(chars)

    for i in range(n):
        max_index = i

        for j in range(i + 1, n):
            if freq[chars[j]] > freq[chars[max_index]]:
                max_index = j

        chars[i], chars[max_index] = chars[max_index], chars[i]

    result = ""

    for ch in chars:
        count = 0
        while count < freq[ch]:
            result += ch
            count += 1

    return result


s = "tree"
print(frequency_sort(s))