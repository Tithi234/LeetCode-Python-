class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total_sum = sum(nums)   # Step 1: total sum of array
        left_sum = 0            # Step 2: running sum from left

        for i in range(len(nums)):
            # right sum = total - left - current element
            right_sum = total_sum - left_sum - nums[i]

            if left_sum == right_sum:   # Step 3: check pivot condition
                return i   # found pivot index

            left_sum += nums[i]  # move to next index

        return -1   # no pivot index found
