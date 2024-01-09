class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.rstrip()
        s = s.lstrip()
        the_list = s.split(" ")
        return len(the_list[-1])

Solution.lengthOfLastWord