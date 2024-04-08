class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip()  # Remove leading spaces
        if not s:  # If string is empty, return 0
            return 0

        # Check if the first character is a sign
        sign = '+'
        if s[0] in ['-', '+']:
            sign = s[0]
            s = s[1:]

        # Extract the number from the string
        num = ''
        for ch in s:
            if ch.isdigit():
                num += ch
            else:
                break

        # If no digits were found, return 0
        if not num:
            return 0

        # Convert the number string to an integer, apply the sign, and clamp to the range of a 32-bit signed integer
        try:
            res = int(sign + num)
            res = max(min(res, 2**31 - 1), -2**31)
        except ValueError:  # If the number string is too large to convert to an integer, return the maximum or minimum value depending on the sign
            res = 2**31 - 1 if sign == '+' else -2**31

        return res