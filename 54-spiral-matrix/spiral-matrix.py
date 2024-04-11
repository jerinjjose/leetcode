class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []

        result = []
        numRows, numCols = len(matrix), len(matrix[0])
        topRow, bottomRow, leftCol, rightCol = 0, numRows - 1, 0, numCols - 1

        while len(result) < numRows * numCols:
            # Traverse from left to right along the top-most row that hasn't been traversed yet.
            for col in range(leftCol, rightCol + 1):
                result.append(matrix[topRow][col])
            topRow += 1  # Update the top-most row that hasn't been traversed yet.

            if len(result) < numRows * numCols:
                # Traverse from top to bottom along the right-most column that hasn't been traversed yet.
                for row in range(topRow, bottomRow + 1):
                    result.append(matrix[row][rightCol])
                rightCol -= 1  # Update the right-most column that hasn't been traversed yet.

            if len(result) < numRows * numCols:
                # Traverse from right to left along the bottom-most row that hasn't been traversed yet.
                for col in range(rightCol, leftCol - 1, -1):
                    result.append(matrix[bottomRow][col])
                bottomRow -= 1  # Update the bottom-most row that hasn't been traversed yet.

            if len(result) < numRows * numCols:
                # Traverse from bottom to top along the left-most column that hasn't been traversed yet.
                for row in range(bottomRow, topRow - 1, -1):
                    result.append(matrix[row][leftCol])
                leftCol += 1  # Update the left-most column that hasn't been traversed yet.

        return result
