class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""

        # Start with the first string as prefix
        prefix = strs[0]

        for s in strs[1:]:
            # Reduce prefix length until it matches the start of s
            while not s . startswith(prefix):
                prefix = prefix[: -1] # remove last character
                if not prefix:
                    return ""

        return prefix
