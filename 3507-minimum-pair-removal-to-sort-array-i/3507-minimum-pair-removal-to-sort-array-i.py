class Solution:
    def minimumPairRemoval(self, nums):
        ops = 0

        while True:
            sorted_ok = True
            for i in range(len(nums) - 1):
                if nums[i] > nums[i + 1]:
                    sorted_ok = False
                    break

            if sorted_ok:
                return ops

            min_sum = nums[0] + nums[1]
            idx = 0
            for i in range(1, len(nums) - 1):
                s = nums[i] + nums[i + 1]
                if s < min_sum:
                    min_sum = s
                    idx = i

            nums[idx] = min_sum
            nums.pop(idx + 1)
            ops += 1