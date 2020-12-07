from typing import List
class FinalPriceWithDiscount:
    def finalPrices(self, prices: List[int]) -> List[int]:
        for i in range(len(prices)):
            j = i + 1
            while j < len(prices) and prices[j] > prices[i]:
                j += 1
            if j < len(prices):
                prices[i] -= prices[j]
        return prices

    def finalPrices2(self, prices: List[int]) -> List[int]:
        final_discount = []
        for i in range(len(prices)):
            found = False
            for j in range(i+1, len(prices)):
                if prices[i] >= prices[j]:
                        found = True
                        final_discount.append(prices[i]-prices[j])
                        break
            if not found:
                final_discount.append(prices[i])
        return final_discount

    def finalPrices3(self, prices: List[int]) -> List[int]:
        stk = []
        for i, p in enumerate(prices):
            while stk and prices[stk[-1]] >= p:
                prices[stk.pop()]-=p
            stk.append(i)
        return prices