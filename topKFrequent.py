def topKFrequent(words, k):
    """
    Problem Description:
    Given a non-empty list of words, return the k most frequent elements.
    Your answer should be sorted by frequency from highest to lowest. If
    two words have the same frequency, then the word with the lower alph-
    abetical order comes first.
    Source: https://leetcode.com/problems/top-k-frequent-words/
    Solution:
    Only achieve an O(n log(n)) method. In general, use heap could achieve an O(n log(k)) time complexity.
    ,but python heapq not support fixed size heap, which making use heaqp to solve in python only could
    achieve O(n log(n))
    :type words: List[str]
    :type k: int
    :rtype: List[str]
    """

    # O(nlog(n)),sorted
    res = dict()
    for word in words:
        if word not in res.keys():
            res[word] = 0
        res[word] += 1
    a = sorted(list(res.items()), key=lambda x: (-x[1], x[0]))
    return [x[0] for x in a[0:k]]




print(topKFrequent(['wo','wo','ai','ai','ni'],2))