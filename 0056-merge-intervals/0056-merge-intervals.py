class Solution:
    def merge(self, intervals):
        intervals.sort()
        ans = [intervals[0]]

        for i in range(1, len(intervals)):
            start, end = intervals[i]

            if start <= ans[-1][1]:
                ans[-1][1] = max(ans[-1][1], end)
            else:
                ans.append([start, end])

        return ans