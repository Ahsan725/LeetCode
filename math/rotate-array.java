class Solution {
    public void rotate(int[] nums, int k) {
        int n = nums.length;
        k = k % n; // Handle cases where k is greater than the length of the array
        
        int[] temp = new int[n]; // Correct array instantiation
        
        // Rotate the last k elements to the right
        int startingIndexFromTheBack = n-k;
        for (int i = 0; i < k; i++) {
            temp[i] = nums[startingIndexFromTheBack + i];
        }
        
        // Rotate the remaining elements
        for (int i = k; i < n; i++) {
            temp[i] = nums[i - k];
        }

        // Update the original array with the rotated values
        for (int i = 0; i < n; i++) {
            nums[i] = temp[i];
        }
    }
}
