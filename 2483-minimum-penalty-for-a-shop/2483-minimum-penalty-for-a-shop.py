class Solution:
    def bestClosingTime(self, customers: str) -> int:
        n = len(customers)
        pre_no = [0 for i in range(n)]
        post_yes = [0 for i in range(n)]

        no_count = 0
        for i in range(1,n):
            pre_no[i]=pre_no[i-1] + (customers[i-1] == "N")
        
        post_yes[-1] = int(customers[-1] == "Y")
        for i in range(n-2,-1,-1):
            post_yes[i] = post_yes[i+1] + (customers[i] == "Y")

        pre_no.append(pre_no[-1])
        post_yes.append(0)
        cost = float("inf")
        rest = 0
        for i in range(n+1):
            left = pre_no[i-1] if i > 0 else 0
            right = post_yes[i]
            if left + right < cost:
                cost = left + right
                res = i
                
        return res