class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        def clean(email):
            local = ""
            domain = ""
            flag = True
            i = 0
            while i < len(email):
                if email[i] == ".":
                    i+=1
                    continue
                if email[i] == "+":
                    while i < len(email) and email[i]!="@":
                        i+=1
                    domain = email[i:]
                    break
                if email[i] == "@":
                    domain = email[i:]
                    break
                local+=email[i]
                i+=1
            return local+domain
                    
        
        email_set = set()
        for email in emails:
            email_set.add(clean(email))
        
        return len(email_set)