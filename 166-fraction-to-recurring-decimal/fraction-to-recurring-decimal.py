class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0:
            return "0"
        
        result = []
        
        if (numerator < 0) != (denominator < 0):
            result.append("-")
        
        numerator = abs(numerator)
        denominator = abs(denominator)
        
        result.append(str(numerator // denominator))
        remainder = numerator % denominator
        if remainder == 0:
            return "".join(result)
        
        result.append(".")
        map = {}
        while remainder != 0:
            if remainder in map:
                result.insert(map[remainder], "(")
                result.append(")")
                break
            
            map[remainder] = len(result)
            remainder *= 10
            result.append(str(remainder // denominator))
            remainder %= denominator
        
        return "".join(result)