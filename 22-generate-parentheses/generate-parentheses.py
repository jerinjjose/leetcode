class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def generate(left_remaining: int, right_remaining: int, current_string: str):
            # If we have no more brackets left to place, append the current string to the result
            if left_remaining == 0 and right_remaining == 0:
                result.append(current_string)
                return

            # If we have some left brackets remaining, place one and recurse
            if left_remaining > 0:
                generate(left_remaining - 1, right_remaining, current_string + '(')

            # If we have more right brackets remaining than left (ensuring validity), place one and recurse
            if right_remaining > left_remaining:
                generate(left_remaining, right_remaining - 1, current_string + ')')

        result = []
        generate(n, n, '')
        return result