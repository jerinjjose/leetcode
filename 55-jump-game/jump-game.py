class Solution:
    def canJump(self, nums: List[int]) -> bool:
        inital = 0
        for n in nums:
            if inital < 0:
                return False
            elif n > inital:
                inital = n
            inital -= 1
            
        return True