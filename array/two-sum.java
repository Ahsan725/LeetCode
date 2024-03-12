class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> map = new HashMap<>();
        int[] result = new int[2]; // Corrected initialization

        for(int i = 0; i < nums.length; i++){
            int complement = target - nums[i]; // Corrected variable name

            if(map.containsKey(complement)){ // Corrected method name
                result[0] = map.get(complement); // Corrected method name
                result[1] = i;
                return result; // No need to continue, we found the pair
            }else{
                map.put(nums[i], i); // Storing the current number and its index
            }
        }
        throw new IllegalArgumentException("No two sum solution");
    }
}
