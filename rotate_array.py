class Solution(object) :
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n # In case k > n

        # Helper function to reverse a portion of the array
        def reverse (start, end):
            while start < end:
                nums[start], nums[end], nums[start]
                start += 1
                end -= 1

        # Step 1: Reverse the whole array
        reverse(0, n-1)
        # Step 2: Reverse first k elemexts
        reverse(0, k-1)
        # Step 3: Reverse remaining elements
        reverse(k, n-1)

