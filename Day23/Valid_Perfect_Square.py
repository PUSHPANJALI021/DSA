def is_perfect_square(num):
    if num < 0:
        return False

    low = 0
    high = num

    while low <= high:
        mid = low + (high - low) // 2
        square = mid * mid

        if square == num:
            return True
        elif square < num:
            low = mid + 1
        else:
            high = mid - 1

    return False


num = int(input("Enter a number: "))
print(is_perfect_square(num))