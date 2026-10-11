class Solution:
    def relativeSortArray(self, arr1, arr2):
        count = {}
        for n in arr1:
            count[n] = count.get(n, 0) + 1

        result = []
        for n in arr2:
            result += [n] * count[n]
            del count[n]

        for n in sorted(count):
            result += [n] * count[n]

        return result