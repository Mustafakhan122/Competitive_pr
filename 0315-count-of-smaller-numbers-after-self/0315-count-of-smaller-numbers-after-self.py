class Solution:
    def countSmaller(self, nums):
        vals = sorted(set(nums))
        rank = {}
        for i in range(len(vals)):
            rank[vals[i]] = i + 1

        n = len(vals)
        tree = [0] * (n + 1)
        ans = []

        for num in reversed(nums):
            r = rank[num]

            i = r - 1
            total = 0
            while i > 0:
                total += tree[i]
                i -= i & -i
            ans.append(total)

            i = r
            while i <= n:
                tree[i] += 1
                i += i & -i

        return ans[::-1]