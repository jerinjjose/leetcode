class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        
        max_val = 0
        count = 0
        for i in range(len(arr)):
            max_val = max(max_val, arr[i])
            if max_val == i:
                count += 1
        return count
        