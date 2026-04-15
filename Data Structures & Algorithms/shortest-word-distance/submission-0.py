class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        i, j = -1, -1
        minDistance = len(wordsDict)
        for n in range(len(wordsDict)):
            if wordsDict[n] == word1:
                i = n
            elif wordsDict[n] == word2:
                j = n
            if i != -1 and j != -1:
                minDistance = min(minDistance, abs(i - j))
        return minDistance