class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        new = [0]*len(candies)
        m = max(candies)
        for i in range(len(candies)):
            tmp = candies[i]+extraCandies
            if tmp>=m:
                new[i] = True
            else:
                new[i] = False
        return new