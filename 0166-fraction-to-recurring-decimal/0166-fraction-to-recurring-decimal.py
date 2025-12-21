class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        negative = ((numerator<0) and (denominator>0)) or ((numerator>0) and (denominator<0))
        numerator = abs(numerator)
        denominator = abs(denominator)
        res = []
        hash = {0:2} #(remainder,index)

        res.append(str(numerator//denominator))
        res.append(".")
        numerator%=denominator

        while True:
            if numerator in hash:
                if numerator != 0:
                    res.insert(hash[numerator],"(")
                    res.append(")")
                break

            hash[numerator] = len(res)
            numerator%=denominator
            numerator*=10
            if numerator:
                res.append(str(numerator//denominator))
        
        if res[-1] == ".":
            res.pop()
        if negative:
            res.insert(0,"-")
        return "".join(res)

