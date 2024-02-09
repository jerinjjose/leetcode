class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        output = strs[0]
        l,r = 0,1
        while r < len(strs):
            if len(strs[l]) <= len(strs[r]):
                n = len(strs[l])
            else:
                n = len(strs[r])

            temp = ""
            for i in range(0,n):
                if strs[l][i] == strs[r][i]:
                    temp += strs[l][i]
                else:
                    break 

            if len(temp) < len(output):
                output = temp 

            r += 1

        return output    