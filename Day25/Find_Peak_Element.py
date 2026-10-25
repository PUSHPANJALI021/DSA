class Solution:
    def findPeakElement(self, nums):
        left = 0
        right = len(nums) - 1

        while left < right:
            mid = left + (right - left) // 2

            if nums[mid] < nums[mid + 1]:
                # Rising slope: peak is to the right
                left = mid + 1
            else:
                # Falling slope or peak: peak is at mid or left
                right = mid

        return left


# Example
nums = [1, 2, 3, 1]
obj = Solution()
print(obj.findPeakElement(nums))  # Output: 2