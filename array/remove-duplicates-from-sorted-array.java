class Solution {
    public int removeDuplicates(int[] nums) {
        int index = 0;

        //[2,3,4,2]
        //[2,3,4,2]

        for(int i = 0; i < nums.length; i++){
            if(i == nums.length - 1 || nums[i] != nums[i+1]){
                nums[index] = nums[i];
                index++; 
            }
        }
        return index;
    }
}