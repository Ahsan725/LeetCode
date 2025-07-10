class Solution:
    def hIndex(self, citations: List[int]) -> int:
        
        # key thing is: are there x number of paper with atleast x number of citations
        #overall goal is to find the biggest x for which there is at least x many citations 

        n = len(citations)
        buckets = [0] * (n + 1)

        for c in citations:
            buckets[min(c, n)] += 1
        
        count = 0
        for i in range(n, -1, -1): #start backwards
            count += buckets[i]
            if count >= i:
                return i
        return 0

            




             

            
