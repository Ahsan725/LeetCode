class Solution {
    public int removeDuplicates(int[] nums) {
        int index = 1;

        //[2,3,4,2]
        //[2,3,4,2]

        for(int i = 1; i < nums.length; i++){
            if(nums[i] != nums[i-1]){
                nums[index] = nums[i];
                index++; 
            }
        }
        return index;
    }
}