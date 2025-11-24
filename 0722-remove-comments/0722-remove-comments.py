class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        
        def remove(pre_comment, line):
            code = ""
            new_line = False
            if pre_comment != "/*":
                pre_comment = ""

            i = 0
            while i < len(line):
                if pre_comment == "/*":
                    if i < len(line)-1 and line[i]+line[i+1] == "*/":
                        pre_comment = ""
                        i+=2
                        if i == len(line):
                            new_line = True
                    else:
                        i+=1
                else:
                    if i < len(line)-1 and line[i]+line[i+1] == "//":
                        pre_comment = ""
                        new_line = True
                        break
                    elif i < len(line)-1 and line[i]+line[i+1] == "/*":
                        pre_comment = "/*"
                        i+=2
                    else:
                        code+=line[i]
                        i+=1
                        if i == len(line):
                            new_line = True
            return code,pre_comment,new_line

        pre_com = ""
        pure_code = ""
        output = []
        for ln in source:
            code,pre_c,new_l = remove(pre_com, ln)

            pre_com = pre_c
            pure_code+=code
            if new_l and pure_code:
                output.append(pure_code)
                pure_code=""
        if pure_code:
            output.append(pure_code)

        return output