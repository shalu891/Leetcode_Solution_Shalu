class Solution(object):
    def maximumSaleItems(self, items, budget):
        max_f = 1500
        freq = [0] * (max_f + 1)
        for f, _ in items:
            freq[f] += 1
            
        div_count = [0] * (max_f + 1)
        for f in range(1, max_f + 1):
            if freq[f] > 0:
                for multiple in range(f, max_f + 1, f):
                    div_count[f] += freq[multiple]
                div_count[f] -= 1
                    
        dp = [0] * (budget + 1)
        
        for f, p in items:
            if p > budget:
                continue
            gain = 1 + div_count[f]
            for b in range(budget, p - 1, -1):
                if dp[b - p] + gain > dp[b]:
                    dp[b] = dp[b - p] + gain
                    
        min_p = min(p for _, p in items)
        
        ans = 0
        for b in range(budget + 1):
            rem = budget - b
            ans = max(ans, dp[b] + rem // min_p)
            
        return ans
        