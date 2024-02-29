class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        
        previous_sequence = self.countAndSay(n - 1)
        result = ""
        current_char = previous_sequence[0]
        count = 1
        
        for i in range(1, len(previous_sequence)):
            if previous_sequence[i] == current_char:
                count += 1
            else:
                result += str(count)
                result += str(current_char)
                current_char = previous_sequence[i]
                count = 1
        
        result += str(count)
        result += str(current_char)
        
        return result