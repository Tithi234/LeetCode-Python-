class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        # safe, works in Python 2 and 3
        return " ".join([word[::-1] for word in s.split()])

if __name__ == "__main__":
    sol = Solution()
    print(sol.reverseWords("Let's take LeetCode contest"))  # s'teL ekat edoCteeL tsetnoc
    print(sol.reverseWords("Mr Ding"))                      # rM gniD


