class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        result = []
        if not matrix or not matrix[0]:
            return result

        top, bottom = 0, len(matrix) - 1
        left, right = 0, len(matrix[0]) - 1

        while top <= bottom and left <= right:
            # Traverse left to right
            for col in range(left, right + 1):
                result.append(matrix[top][col])
            top += 1

            # Traverse top to bottom
            for row in range(top, bottom + 1):
                result.append(matrix[row][right])
            right -= 1

            # Traverse right to left
            if top <= bottom:
                for col in range(right, left - 1, -1):
                    result.append(matrix[bottom][col])
                bottom -= 1

            # Traverse bottom to top
            if left <= right:
                for row in range(bottom, top - 1, -1):
                    result.append(matrix[row][left])
                left += 1

        return result


# Testing the code
if __name__ == "__main__":
    sol = Solution()
    mat1 = [[1,2,3],[4,5,6],[7,8,9]]
    mat2 = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
    print(sol.spiralOrder(mat1))  # Output: [1,2,3,6,9,8,7,4,5]
    print(sol.spiralOrder(mat2))  # Output: [1,2,3,4,8,12,11,10,9,5,6,7]
