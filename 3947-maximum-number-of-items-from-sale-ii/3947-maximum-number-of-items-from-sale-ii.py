class Solution(object):
    def maximumSaleItems(self, items, budget):
        n = len(items)
        freq = [0] * (n + 1)
        for factor, _ in items:
            freq[factor] += 1

        div_count = [0] * (n + 1)
        for f in range(1, n + 1):
            if freq[f]:
                for m in range(f, n + 1, f):
                    div_count[f] += freq[m]

        min_price = min(price for _, price in items)
        batches = []
        for factor, price in items:
            gain = div_count[factor] - 1
            if gain > 0 and price < 2 * min_price:
                batches.append((price, gain))

        batches.sort()

        total_items = 0
        for price, gain in batches:
            if budget < price:
                break
            can_buy = min(gain, budget // price)
            total_items += 2 * can_buy
            budget -= can_buy * price

        total_items += budget // min_price

        return total_items