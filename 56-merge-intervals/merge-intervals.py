class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) < 2:
            return intervals

        intervals = sorted(intervals, key=lambda x: x[0])
        result = []
        currentArray = intervals[0]

        for index in range(1, len(intervals)):
            if currentArray[1] >= intervals[index][0]:  # overlap
                currentArray[1] = max(intervals[index][1], currentArray[1])
            else:
                result.append(currentArray)
                currentArray = intervals[index]

        result.append(currentArray)
        return result