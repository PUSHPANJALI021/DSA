def sort_by_frequency(s):
    freq = {}

    for ch in s:
        if ch in freq:
            freq[ch] = freq[ch] + 1
        else:
            freq[ch] = 1

    chars = []

    for ch in freq:
        chars.append(ch)

    n = len(chars)

    for i in range(n - 1):
        largest = i

        for j in range(i + 1, n):
            if freq[chars[j]] > freq[chars[largest]]:
                largest = j

        temp = chars[i]
        chars[i] = chars[largest]
        chars[largest] = temp

    result = ""

    for ch in chars:
        for _ in range(freq[ch]):
            result += ch

    return result


s = "banana"
print(sort_by_frequency(s))