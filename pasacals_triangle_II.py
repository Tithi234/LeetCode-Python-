class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        row = [1] #First row is always [1]

        for i in range(1, rowIndex + 1):
            # Update the row in reverse in reverse to avoid overwriting
            row.append(0) # Extend row for the new element
            for j in range(i, 0, -1):
                row[j] += row[j-1]

        return row


