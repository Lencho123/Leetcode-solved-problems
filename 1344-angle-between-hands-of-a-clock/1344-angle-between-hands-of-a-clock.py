class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        start = (hour*5)%60 + (minutes/60)*5
        end = minutes

        dist = abs(start-end)
        cand = 180*dist/30
        return min(cand, 360-cand)