class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False
        else:
            max_int = 3**19 
            if (max_int % n) == 0:
                return True
            else:
                return False
