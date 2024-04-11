class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        n = len(matrix)
        
        # Process layer by layer, starting from the outer layer
        for i in range(n // 2):
            # For each layer, move the elements of four symmetric positions in a circular way
            for j in range(i, n - i - 1):
                # Store the top element temporarily
                temp = matrix[i][j]
                
                # Move the left element to the top
                matrix[i][j] = matrix[n - j - 1][i]
                
                # Move the bottom element to the left
                matrix[n - j - 1][i] = matrix[n - i - 1][n - j - 1]
                
                # Move the right element to the bottom
                matrix[n - i - 1][n - j - 1] = matrix[j][n - i - 1]
                
                # Move the top element (stored in temp) to the right
                matrix[j][n - i - 1] = temp