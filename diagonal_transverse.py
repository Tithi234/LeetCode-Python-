class Solution(object):
    def findDiagonalOrder(self, mat):
        if not mat or not mat[0]:
            return []

        m, n = len(mat), len(mat[0])
        result = []

        for d in range(m + n - 1):
            temp = []
            r = 0 if d < n else d - n + 1
            c = d if d < n else n - 1

            while r < m and c >= 0:
                temp.append(mat[r][c])
                r += 1
                c -= 1

            if d % 2 == 0:
                result.extend(temp[::-1])
            else:
                result.extend(temp)

        return result

# Testing the code
if __name__ == "__main__":
    sol = Solution()
    mat1 = [[1,2,3],[4,5,6],[7,8,9]]
    mat2 = [[1,2],[3,4]]
    print(sol.findDiagonalOrder(mat1))  # Output: [1,2,4,7,5,3,6,8,9]
    print(sol.findDiagonalOrder(mat2))  # Output: [1,2,3,4]
