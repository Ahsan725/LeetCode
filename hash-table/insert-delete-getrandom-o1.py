class RandomizedSet:

    #lets look at possible data structures we can use:
    #linked list -> insert O(1), remove O(n), getRandom O(n)
    #HashSet -> insert O(1), remove O(1), getRandomo(N)
    #List -> insertO(1), remove O(n), getRandom O(1)
    #hashmap -> insert O(1), remove O(1), O(n)
    #combining two data structures


    def __init__(self):
        self.nummap = {}
        self.numlist = []
        #map {key= the data, value=the index in the list}
        

    def insert(self, val: int) -> bool:
        res = val not in self.nummap 
        if res:
            self.nummap[val] = len(self.numlist) #
            self.numlist.append(val)
        return res
    
    def remove(self, val: int) -> bool:
        res = val in self.nummap
        if res:
            index = self.nummap[val]
            last_element = self.numlist.pop()
            self.numlist[index] = last_element
            self.nummap[last_element] = index
            del self.nummap[val]
        
        return res
        
    def getRandom(self) -> int:

        return random.choice(self.numlist)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()