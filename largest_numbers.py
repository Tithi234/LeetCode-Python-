class Solution:
    def dominantIndex(self, nums):
        # Step 1: Find the largest number
        max_num = max(nums)
        # Step 2: Find the index of the largest number
        max_index = nums.index(max_num)

        # Step 3: Check the "at least twice" condition for every other number
        for i, num in enumerate(nums):
            if i != max_index and max_num < 2 * num:
                return -1  # Condition fails for some number

        # Step 4: If the loop completes, return the index of the largest number
        return max_index
