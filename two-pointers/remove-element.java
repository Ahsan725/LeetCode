class Solution {
    public int removeElement(int[] nums, int val) {
        //we need to do this in place
        //I am thinking of doing a for loop which checks for the values and then reasisgns
        //for example: if [3,4,2,5,2,2,1,6] i = 5, idx = 5
        //                [3,4,6,5,1,2,2,2]
        // val = 3
        // sample test case: [3,2,2,3] last_index = 1, i = 1
        // sample test case: [2,2,3,3] 
        //[3,3] last index = 0, i = 0

        // int[] empty = new int[];
        int numSwaps = 0;
        int last_index = nums.length-1;
        if(nums.length == 1 && nums[0] == val){ // Set the array to an empty array
                return 0;
            }
        for(int i = 0; i < nums.length -1; i++){

            if(nums[last_index] == val){
                last_index--;
            }
            
            if(nums[i] == val && i < last_index ){
                int temp = nums[i];
                nums[i] = nums[last_index];
                nums[last_index] = temp;
                last_index--; 
                swap++;
            }
            if(numSwaps > 2){
                return 0;
            }
        }
        return last_index + 1;
    }
}