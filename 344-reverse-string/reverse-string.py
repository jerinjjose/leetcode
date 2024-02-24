class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        if len(s) > 1:

            index = 0
            while (len(s)) // 2 > index:
                temp = s[index]
                s[index] = s[(len(s) - 1 ) - index]
                s[(len(s) - 1 ) - index] = temp
                index +=1
