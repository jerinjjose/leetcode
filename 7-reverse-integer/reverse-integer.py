class Solution:
    def reverse(self, x: int) -> int:
        upper_limit = (2 ** 31) -1 #to check the maxximum limit.
        ouput = 0
        is_negative = x < 0
        if is_negative:
            x = -x
        while x > 0:
            last_digit = x % 10
            if ouput > (upper_limit - last_digit) // 10:
                return 0
            ouput = ouput * 10 + last_digit
            x = x // 10
        
        if is_negative:
            ouput = -ouput
        return ouput



