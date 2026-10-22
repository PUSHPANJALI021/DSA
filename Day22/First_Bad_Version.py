def isBadVersion(version):
    return version >= first_bad


def firstBadVersion(n):
    low = 1
    high = n

    while low < high:
        mid = low + (high - low) // 2

        if isBadVersion(mid):
            high = mid

        else:
            low = mid + 1

    return low


n = int(input("Enter total versions: "))
first_bad = int(input("Enter first bad version: "))

print("First bad version:", firstBadVersion(n))