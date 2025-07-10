class Solution:
    def hIndex(self, citations: List[int]) -> int:
        #Understanding: h index as I understand is the number of papers that have been cited at least 
        #that many times
        #Approach:
        #iterating over the array I am looking for a number where there is at least that many numbers or bigger
        #maybe using a hashmap here culd help me? 3:(3), 0(5), 6(1), 1(4), 5(2) -> 0, 5, 5, 3, 3
        #the number itself must be smaller than or equal to the counts otherwise not valid
        #once you have this you need to return the number whose count - the number itself is smallest 
        
        if len(citations) == 1 and citations[-1] == 0:
            return 0
        if len(citations) == 1:
            return 1

        cite_to_num_of_nums_equal_bigger = {}
        valid_keys =[]
        smallest_abs = float('inf')
        smallest_key = float('inf')

        for c in citations:
            #how many numbers are greater than c?
            count = 0
            for b in citations:
                if b >= c:
                    count += 1
                cite_to_num_of_nums_equal_bigger[c] = count
        
        for key, value in cite_to_num_of_nums_equal_bigger.items():
            if key <= value:
                valid_keys.append(key)
        for key in valid_keys:
            abs_val = abs(key - cite_to_num_of_nums_equal_bigger[key])
            if abs_val < smallest_abs:
                smallest_abs = abs_val
                smallest_key = key

        return smallest_key
            




             

            
