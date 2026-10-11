from functools import cmp_to_key

class Solution:
    def largestNumber(self, nums):
        arr = [str(x) for x in nums]

        def compare(a, b):
            if a + b > b + a:
                return -1
            elif a + b < b + a:
                return 1
            return 0

        arr.sort(key=cmp_to_key(compare))

        if arr[0] == "0":
            return "0"

        return "".join(arr)