class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        # If needle is empty, return 0
        if not needle:
            return 0

        len_h, len_n = len(haystack), len(needle)

        for i in range(len_h - len_n + 1):
            if haysatck[i:i+len_n] == needle:
                    return i

        return -1



