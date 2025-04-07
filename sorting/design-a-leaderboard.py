#Understanding: we have to create a leaderboard and implement some functions. some observatrions I have made are that
#we are adding at the end, when we call reset it removes from the leaderboard. 
#Approach: since we are appending at the end we can use a list and add tuples to represent the id and the score
#addscore -> O(1),
#reset -> Map key ?  use a list to make topk efficent a heap and maintain a heap of n values (worst case) 
#Main = Map {key:id, value:score}, Heap(tuple(id, score)) -> maxheap -(9) 73->56 pid:1 adscore(1,23), addscore(1,20)
#better? map -> top iteratve over the map and create a maxheap of k 
class Leaderboard:

    def __init__(self):
        self.leader = {}

    def addScore(self, playerId: int, score: int) -> None: #O(1)
        if playerId in self.leader:
            #we update
            self.leader[playerId] += score
        else:
            #we add
            self.leader[playerId] = score

    def top(self, K: int) -> int: #O(nlogk) where k <= to n O(k)
        sumscore = 0
        scores = [-val for val in list(self.leader.values())] #syntax review 
        heapq.heapify(scores) #create a max heap #syntax review
        for i in range(K):
            value = heapq.heappop(scores)
            sumscore += (value * -1) #negating to return to original value
        return sumscore

    def reset(self, playerId: int) -> None: #O(1)
        if playerId in self.leader:
            #we remove
            del self.leader[playerId]

#feedback: everytime you see topk -> always use the heap. Global vs when method is called? -> if the values that you are creating a heap for are changing dynamically then there is n o point to create heap early
#Critical Feedback: always wanna use tuple for no reason. keep the key value as simple / primitive as possible. Only do it when absoluetly necessary. 

# Your Leaderboard object will be instantiated and called as such:
# obj = Leaderboard()
# obj.addScore(playerId,score)
# param_2 = obj.top(K)
# obj.reset(playerId)