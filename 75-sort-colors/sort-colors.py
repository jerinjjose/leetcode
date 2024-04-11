class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        red = []
        white = []
        blue = []
        for number in nums:
            if number == 0:
                red.append(number)
            elif number == 1:
                white.append(number)
            else:
                blue.append(number)
        nums[:] = red + white + blue
