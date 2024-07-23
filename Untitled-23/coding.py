class Solution(object):
    def checkIfPangram(self, sentence):
        """
        :type sentence: str
        :rtype: bool
        """
        d = set()
        [d.add(i) for i in sentence.lower()]
        return len(d) == 26


sol = Solution()

print(sol.checkIfPangram("thequickbrownfoxjumpsoverthelazydog"))
