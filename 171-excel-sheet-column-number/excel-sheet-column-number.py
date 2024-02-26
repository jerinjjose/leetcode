class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        ans = 0
        pos = 0
        for letter in reversed(columnTitle):
            digit = ord(letter)-64 # function to get the unicode No. A-Z is 65-90
            ans += digit * 26**pos
            pos += 1
            
        return ans