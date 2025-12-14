class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letters = []
        digits = []
        
        for log in logs:
            if not log[-1].isdigit():
                letters.append(log)
            else:
                digits.append(log)
                
        for i,log in enumerate(letters):
            letters[i] = log.split()
            
        letters.sort(key=lambda log: (log[1:], log[0]))
        
        for i,log in enumerate(letters):
            letters[i] = " ".join(log)
                
        return letters+digits