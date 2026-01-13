class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        
        def calculate(p):
            area_below = 0
            area_above = 0
            h_below = 0
            h_above = 0

            for x,y,h in squares:
                if p <= y:
                    h_above = h
                    h_below = 0
                elif p <= y+h:
                    h_above = y+h-p
                    h_below = p-y
                else:
                    h_above = 0
                    h_below = h

                area_below+=h_below*h
                area_above += h_above*h
            
            return area_below, area_above

        l = 0 
        r = 10**10

        m = 0
        while r - l > 1e-6:
            m = (l + r) / 2
            area_below, area_above = calculate(m)

            if area_above > area_below:
                l = m
            else:
                r = m
        
        return (l + r) / 2