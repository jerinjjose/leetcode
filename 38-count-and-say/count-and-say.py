class Solution:
    def countAndSay(self, n: int) -> str:
        countString = "1"
        for _ in range(n - 1):
            countString = self.countTheString(countString)
        return countString

    def countTheString(self, count: str) -> str:
        formattedString = []
        counter = 1
        prev = count[0]
        for index in range(1, len(count)):
            if count[index] == prev:
                counter += 1
            else:
                formattedString.append(str(counter))
                formattedString.append(prev)
                counter = 1
                prev = count[index]
        formattedString.append(str(counter))
        formattedString.append(prev)
        return ''.join(formattedString)