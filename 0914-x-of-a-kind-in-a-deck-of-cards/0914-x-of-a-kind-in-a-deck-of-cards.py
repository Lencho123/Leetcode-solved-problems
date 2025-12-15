class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        count = Counter(deck)
        
        def factorize(num):
            factors = set()
            d = 2
            while num > 1:
                while num%d == 0:
                    num/=d
                    factors.add(d)
                d+=1
            return list(factors)
        
        all_factors = []
        for freq in list(count.values()):
            all_factors.extend(factorize(freq))
        factor_freq = Counter(all_factors)
        
        for key in factor_freq:
            if factor_freq[key] == len(count):
                return True
        return False