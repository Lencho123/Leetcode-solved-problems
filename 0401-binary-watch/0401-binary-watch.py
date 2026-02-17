class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        if turnedOn == 0:
            return ["0:00"]
        
        def hDfs(call_count,turned_on_count,time):
            if call_count == 4 and turned_on_count == 0 and time <= 11:
                time_set.add(time)
                return
            if call_count > 4 or turned_on_count < 0 or time > 11:
                return
            
            # set bit
            hDfs(call_count+1,turned_on_count-1,time+(2**(3-call_count)))
            # not set bit
            hDfs(call_count+1,turned_on_count,time)

        
        def mDfs(call_count,turned_on_count,minute):
            if call_count == 6 and turned_on_count == 0 and minute <= 59:
                minute_set.add(minute)
                return
            if call_count > 6 or turned_on_count < 0 or minute > 59:
                return
            
            # print(call_count,turned_on_count,minute)
            # set bit
            mDfs(call_count+1,turned_on_count-1,minute+(2**(5-call_count)))
            # not set bit
            mDfs(call_count+1,turned_on_count,minute)

        
        res = set()
        def merge(times,minutes):
            for t in times:
                tm = str(t)
                for m in minutes:
                    mn = str(m) if len(str(m)) == 2 else "0"+str(m)

                    res.add(tm+":"+mn)

        for i in range(turnedOn):
            minute_set = set()
            time_set = set()
            hDfs(0,i,0)
            mDfs(0,turnedOn-i,0)
            merge(time_set, minute_set)

            minute_set = set()
            time_set = set()
            mDfs(0,i,0)
            hDfs(0,turnedOn-i,0)
            merge(time_set, minute_set)
        
        res = list(res)
        return res