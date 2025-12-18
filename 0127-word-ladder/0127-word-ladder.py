class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

        wordList = set(wordList)
        wordList.add(beginWord)

        # Let us construct graph frowm the wordlist using given information
        graph = defaultdict(list)
        for word in wordList:
            for j in range(len(word)):
                for i in range(26):
                    char = chr(ord("a")+i)
                    if char != word[j]:
                        u = word[:j] + char + word[j+1:]
                        if u in wordList:
                            graph[word].append(u)
                            graph[u].append(word)

        
        # Use bfs to find shortest path betwen star and end word
        que = deque([beginWord])
        visited = set([beginWord])

        res = 1
        while que:
            l = len(que)
            flag = True
            for i in range(l):
                p = que.popleft()
                for nei in graph[p]:
                    if nei not in visited:
                        visited.add(nei)
                        que.append(nei)
                if p == endWord:
                    return res
            res+=1

        return 0