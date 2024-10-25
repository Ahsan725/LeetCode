class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        #record the frequency in a map
        #sort the map
        #return the keys with value == k
        freq_map = {}
        res = []
        for wrd in words:
            freq_map[wrd] = freq_map.get(wrd,0) + 1
        sorted_items = sorted(freq_map.items(), key= lambda x: (-x[1], x[0]))
        #[a,b,d,g,x]. # map = {x:4,a:3,g:22,d:89,b:34}
        for word, freq, in sorted_items[:k]:
            res.append(word) #we dont need the freq we just used it so we can extarct the two val
        return res        
        