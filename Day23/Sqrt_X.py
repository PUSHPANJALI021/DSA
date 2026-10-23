def my_sqrt(x):
    if x < 2:
        return x

    low = 1
    high = x
    answer = 0

    while low <= high:
        mid = low + (high - low) // 2

        if mid * mid == x:
            return mid

        elif mid * mid < x:
            answer = mid
            low = mid + 1

        else:
            high = mid - 1

    return answer


x = int(input("Enter a non-negative integer: "))
print("Square root:", my_sqrt(x))