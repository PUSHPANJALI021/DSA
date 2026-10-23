def guess(num):
    if num == picked:
        return 0
    elif num > picked:
        return -1
    else:
        return 1


def guess_number(n):
    low = 1
    high = n

    while low <= high:
        mid = low + (high - low) // 2
        result = guess(mid)

        if result == 0:
            return mid
        elif result == -1:
            high = mid - 1
        else:
            low = mid + 1

    return -1


n = int(input("Enter n: "))
picked = int(input("Enter the picked number: "))

print("Guessed number:", guess_number(n))