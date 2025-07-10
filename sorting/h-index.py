class Solution:
    def hIndex(self, citations: List[int]) -> int:
        #Understanding: h index as I understand is the number of papers that have been cited at least 
        #that many times
        #Approach:
        #iterating over the array I am looking for a number where there is at least that many numbers or bigger
        #maybe using a hashmap here culd help me? 3:(3), 0(5), 6(1), 1(4), 5(2) -> 0, 5, 5, 3, 3
        #the number itself must be smaller than or equal to the counts otherwise not valid
        #once you have this you need to return the number whose count - the number itself is smallest 
        
        # key thing is: are there x number of paper with atleast x number of citations
        #overall goal is to find the biggest x for which there is at least x many citations 

        n = len(citations)
        buckets = [0] * (n + 1)

        for c in citations:
            buckets[min(c, n)] += 1
        
        count = buckets[-1]
        num = (n)
        while num > count:
            count += buckets[num]
            num -= 1
        num = num -1 
        if num >= 0:
            return num
        else:
            0

            




             

            
