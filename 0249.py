class Solution(object):
    def groupStrings(self, strings):
        """
        :type strings: List[str]
        :rtype: List[List[str]]
        """
        groups = collections.defaultdict(list)
        for s in strings:
            groups[tuple((ord(c)-ord(s[0])) % 26 for c in s)].append(s)
        print(groups)
        return groups.values()
