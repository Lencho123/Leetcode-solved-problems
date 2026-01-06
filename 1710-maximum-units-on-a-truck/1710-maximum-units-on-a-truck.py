class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key = lambda x: -x[1])
        print(boxTypes)

        total_units = 0
        for b,u in boxTypes:
            if truckSize >= b:
                total_units+=u*b
                truckSize-=b
            elif truckSize > 0:
                total_units+=u*truckSize
                truckSize = 0
            else:
                break

        return total_units