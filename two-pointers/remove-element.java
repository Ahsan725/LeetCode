class Solution {
    public int removeElement(int[] nums, int val) {
        //test case: [3,2,2,3] index = 2, i = 3
        //test case: [2,2,2,3]

        //test case: [3,3] index = 0, i = 2
        //test case: [3,3]
        
        int index = 0;
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] != val) {
                nums[index] = nums[i];
                index++;
            }
        }
        return index;
    }
}