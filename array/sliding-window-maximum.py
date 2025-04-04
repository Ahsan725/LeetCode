class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        q = deque()

        for i in range(len(nums)):

            #only add to q in an increasing order
            while q and nums[q[-1]] < nums[i]:
                q.pop() #keep removing if the cur element is bigger than some prev elems
            q.append(i) #append cur elm

            #remove any out of bounds indices that are less than left ( i -k +1)
            while q and q[0] < i - k + 1:
                q.popleft()
            #once we reach the k window size add to res 
            if i >= k - 1:
                res.append(nums[q[0]])

        return res  