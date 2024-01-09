class Solution:
    import sys
    sys.set_int_max_str_digits(10**9)
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        rep = set()
        for i in nums:
            if i in seen:
               rep.add(i)
            else:
                seen.add(i)
        if rep != set():
            return True
        else:
            return False 