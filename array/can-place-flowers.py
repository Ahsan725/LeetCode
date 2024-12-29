class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:

        res = []
        
        for i in range(len(flowerbed) - 3):
            if flowerbed[i] == 0:
                #when it is 0
                if flowerbed[i+1] == 0 and flowerbed[i+2] == 0:
                    flowerbed[i+1] = 1
                    res.append(True)
                else:
                    res.append(False)
        
        count = 0
        for bol in res:
            if bol == True:
                count += 1
        
        if count == n:
            return True
        else:
            return False
