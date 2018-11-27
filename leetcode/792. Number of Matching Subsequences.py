# Given string S and a dictionary of words words, find the number of words[i] that is a subsequence of S.
import collections
import copy

class Solution:
    def numMatchingSubseq(self, S, words):
        """
        :type S: str
        :type words: List[str]
        :rtype: int
        """
        cnts = 0
        d = collections.defaultdict(set)
        for i, w in enumerate(S):
            d[w].add(i)
        for word in words:
            td = copy.deepcopy(d)
            for c in word:
                if td[c] <= 0:
                    break
                td[c] -= 1
            else:
                cnts += 1
                print(word)
        return cnts


if __name__ == '__main__':
    sl = Solution()
    s = "abcde"
    words = ["a", "bb", "acd", "ace"]
    print(sl.numMatchingSubseq(s, words))
    from collections import defaultdict
    a = set()
    a.remove()

