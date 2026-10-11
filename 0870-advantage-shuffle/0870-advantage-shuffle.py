class Solution:
    def advantageCount(self, nums1, nums2):
        sorted1 = sorted(nums1)
        order = sorted(range(len(nums2)), key=lambda i: nums2[i])

        ans = [0] * len(nums1)
        leftover = []
        j = 0

        for x in sorted1:
            if x > nums2[order[j]]:
                ans[order[j]] = x
                j += 1
            else:
                leftover.append(x)

        for i in order[j:]:
            ans[i] = leftover.pop()

        return ans