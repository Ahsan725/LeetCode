class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:

        res = []
        
        for i in range(len(flowerbed) - 3):
            if flowerbed[i] == 0:
                
                #check if it is teh first value
                if i == 0:
                    if flowerbed[i+1] == 0:
                        flowerbed[i] = 1
                        res.append(True)
                
                elif i == len(flowerbed) - 3:
                    if flowerbed[i+1] == 0 and flowerbed[i+2] == 0:
                        flowerbed[i+2] = 1
                        res.append(True)

                #when it is 0
                elif flowerbed[i+1] == 0 and flowerbed[i+2] == 0:
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
