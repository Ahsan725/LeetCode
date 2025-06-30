class Solution:
    def makeSubKSumEqual(self, arr: List[int], k: int) -> int:
        # we are retuning the number of operations 
        #I think first chalenge will be to figure out how to section subarray off
        ops = 0
        for i in range(1, len(arr)):
            ops += abs(arr[i] - arr[i -1])
        return ops