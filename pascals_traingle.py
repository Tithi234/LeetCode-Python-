class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        triangle = []

        for row in range(numRows):
            # Start each row with 1s
            new_row = [1] * (row + 1)

            # Fill middle values using values from previous row
            for col in range(1, row):
                new_row[col] = triangle[row - 1][col - 1] + triangle[row - 1][col]

            triangle.append(new_row)

        return triangle


# Run tests when file is executed
if __name__ == "__main__":
    sol = Solution()
    print(sol.generate(5))  # [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
    print(sol.generate(1))  # [[1]]

