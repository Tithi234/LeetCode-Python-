class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        result = [0] * n       # create result array of same length
        left = 0               # start pointer
        right = n - 1          # end pointer
        pos = n - 1            # position to fill in result array from end

        while left <= right:
            if abs(nums[left]) > abs(nums[right]):
                result[pos] = nums[left] ** 2
                left += 1
            else:
                result[pos] = nums[right] ** 2
                right -= 1
            pos -= 1           # move backwards in result array

        return result
