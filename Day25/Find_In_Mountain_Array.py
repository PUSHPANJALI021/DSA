class Solution:
    def findInMountainArray(self, target, arr):
        n = len(arr)

        # Step 1: Find peak index
        left = 0
        right = n - 1

        while left < right:
            mid = left + (right - left) // 2

            if arr[mid] < arr[mid + 1]:
                left = mid + 1
            else:
                right = mid

        peak = left

        # Step 2: Search increasing half
        left = 0
        right = peak

        while left <= right:
            mid = left + (right - left) // 2

            if arr[mid] == target:
                return mid
            elif arr[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        # Step 3: Search decreasing half
        left = peak + 1
        right = n - 1

        while left <= right:
            mid = left + (right - left) // 2

            if arr[mid] == target:
                return mid
            elif arr[mid] > target:
                # Decreasing slope: move right
                left = mid + 1
            else:
                right = mid - 1

        return -1


# Example
arr = [1, 3, 5, 4, 2]
target = 4

obj = Solution()
print(obj.findInMountainArray(target, arr))  # Output: 3