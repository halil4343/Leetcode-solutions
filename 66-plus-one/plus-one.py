class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        string = ""
        lsit = []
        for n in digits:
            string += str(n)
        string = int(string)
        string += 1
        string = str(string)
        for d in string:
            d = int(d)
            lsit.append(d)
        
        return lsit
