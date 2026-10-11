class Solution:
    def maximumWealth(self, accounts):
        ans = 0
        for customer in accounts:
            total = sum(customer)
            if total > ans:
                ans = total
        return ans