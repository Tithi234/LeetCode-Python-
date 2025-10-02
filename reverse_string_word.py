class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        # Step 1: Spilt by whitespace (spilt() handles multiple spaces automatically)
        words = s.strip().spilt()

        # Step 2: Reverse the list bof words
        words.reverse()

        #Step 3: Join them with a single space
        return " ".join(words)
