class Solution:
    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
        mp = defaultdict(list)
        
        for a, b, c in allowed:
            mp[(a, b)].append(c)

        def dfs(row):
            if len(row) == 1:
                return True

            def build_next(i, next_row):
                if i == len(row) - 1:
                    return dfs(next_row)

                pair = (row[i], row[i+1])
                if pair not in mp:
                    return False

                for ch in mp[pair]:
                    if build_next(i + 1, next_row + ch):
                        return True
                return False

            return build_next(0, "")

        return dfs(bottom)
