class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = []
        seenIndex = {}
        count = 0
        for string in strs:
            sortedValue = ''.join(sorted(string))
            if sortedValue not in seenIndex:
                seenIndex[sortedValue] = count
                output.append([])
                count +=1
            output[seenIndex[sortedValue]].append(string)
        return output
