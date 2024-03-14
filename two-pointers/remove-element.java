class Solution {
    public int removeElement(int[] nums, int val) {
        //we need to do this in place
        //I am thinking of doing a for loop which checks for the values and then reasisgns
        //for example: if [3,4,2,5,2,2,1,6] i = 5, idx = 5
        //                [3,4,6,5,1,2,2,2]
        // val = 3
        // sample test case: [3,2,2,3] last_index = 1, i = 1
        // sample test case: [2,2,3,3] 

        // int[] empty = new int[];

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