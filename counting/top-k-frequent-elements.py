class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Count the frequency of each number
        counter = Counter(nums)

        # Create a min-heap to store the top k frequent elements
        min_heap = []

        # Iterate through the counts and maintain a heap of size k
        for num, freq in counter.items():
            # Push (freq, num) tuple into the heap
            heapq.heappush(min_heap, (freq, num))
            # If the size of the heap exceeds k, pop the smallest element
            if len(min_heap) > k:
                heapq.heappop(min_heap)

        # Extract the top k frequent elements from the heap
        top_k = [num for freq, num in min_heap]

        return top_k