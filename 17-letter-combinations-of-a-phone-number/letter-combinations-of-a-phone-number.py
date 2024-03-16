class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        numberMap = {
            "2" : ["a","b","c"],
            "3" : ["d","e","f"],
            "4" : ["g","h","i"],
            "5" : ["j","k","l"],
            "6" : ["m","n","o"],
            "7" : ["p","q","r","s"],
            "8" : ["t","u","v"],
            "9" : ["w","x","y","z"]
        }
        def backtrack(index, path):
            if index == len(digits):
                result.append("".join(path))
                return

            for char in numberMap[digits[index]]:
                path.append(char)
                backtrack(index + 1, path)
                path.pop()

        result=[]
        if len(digits) > 0:
            backtrack(0, [])
        return result
        