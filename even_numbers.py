class Solution(object):
    def findNumbers(self, nums):
        counter = 0
        for num in nums:
            digit_count = 0
            temp = num
            # Handle 0 separately
            if temp == 0:
                digit_count = 1
            else:
                while temp > 0:
                    temp = temp // 10
                    digit_count += 1
            # Check if the number of digits is even
            if digit_count % 2 == 0:
                counter += 1
        return counter
