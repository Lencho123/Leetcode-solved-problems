class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        cnt1 = 0
        flag = False
        row = 0
        for i in range(len(bank)):
            for j in range(len(bank[0])):
                if bank[i][j] == "1":
                    cnt1+=1
                    flag = True
            if flag:
                row = i
                break
            
        cnt2 = 0
        res = 0
        for r in range(row+1,len(bank)):
            for c in range(len(bank[0])):
                if bank[r][c] == "1":
                    cnt2+=1
            if cnt2 and cnt1:
                res+=cnt1*cnt2
                cnt1 = cnt2
                cnt2 = 0
        return res