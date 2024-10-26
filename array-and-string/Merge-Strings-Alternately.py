class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        n1 = len(word1)
        n2 = len(word2)
        n = min(n1,n2)
        m = max(n1,n2)
        l = []
        for i in range(n):
            l.append(word1[i])
            l.append(word2[i])
        if n2>n1:
            for i in range(n,m):
                l.append(word2[i])
        if n1>n2:
            for i in range(n,m):
                l.append(word1[i])
        return ''.join(l)