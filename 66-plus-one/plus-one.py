class Solution:
    def plusOne(self, num: List[int]) -> List[int]:
        n = len(num)
        
        # Check if there is no carry after incrementing the last digit
        if num[n - 1] + 1 != 10:
            num[n - 1] += 1
            return num

        # If there is a carry, propagate it to the higher digits
        carry = 1
        for i in range(n - 1, -1, -1):
            num[i] += carry
            if num[i] == 10:
                carry = 1
                num[i] = 0
            else:
                carry = 0
                break

        # If there is still a carry after processing all digits, insert it at the beginning
        if carry:
            num.insert(0, carry)
        
        return num