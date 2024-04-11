class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(start):
            # If we're at the end of the list, we have a complete permutation
            if start == len(nums):
                permutations.append(nums[:])
            else:
                # Swap the current element with each element that comes after it
                for i in range(start, len(nums)):
                    nums[start], nums[i] = nums[i], nums[start]  # swap
                    backtrack(start + 1)  # generate permutations for the rest of the list
                    nums[start], nums[i] = nums[i], nums[start]  # backtrack

        permutations = []
        backtrack(0)
        return permutations