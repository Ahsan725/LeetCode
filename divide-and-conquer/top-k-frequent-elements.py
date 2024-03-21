class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Create a dictionary to store frequency of each number
        freq_map = defaultdict(int)

        # Count the frequency of each number in the list
        for num in nums:
            freq_map[num] += 1

        # Sort the dictionary by values (frequencies) in descending order
        sorted_freq = sorted(freq_map.items(), key=lambda x: x[1], reverse=True)

        # Extract the top k frequent numbers
        top_k = [x[0] for x in sorted_freq[:k]]

        return top_k