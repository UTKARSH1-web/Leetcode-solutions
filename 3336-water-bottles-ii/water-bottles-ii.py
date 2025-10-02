class Solution:
    def maxBottlesDrunk(self, numBottles: int, numexchange: int) -> int:
        drunk = numBottles
        empty = numBottles
        exch = numexchange
        full = 0
        # print(full,empty,exch,drunk)
        while empty>=exch:
            empty = empty - exch
            full+=1
            exch+=1
            if empty<exch and full!=0:
                empty+=full
                drunk+=full
                full=0
            # print(full,empty,exch,drunk)
        return drunk