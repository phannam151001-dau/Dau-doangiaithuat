class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        mp = defaultdict(list)
        for s in strs:
            key = ''.join(sorted(s))
            mp[key].append(s)
        return list(mp.values())
