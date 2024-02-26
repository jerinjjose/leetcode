class Solution:
    def isHappy(self, n: int) -> bool:
        seenObj = {}
        while n !=0 and n not in seenObj:
            seenObj[n] = n
            n = sum(int(i)**2 for i in str(n))
        if n ==1:
            return True
        else:
            return False