class Solution {
    public int removeDuplicates(int[] nums) {
        int index = 1;

        //result.  : [1,1,1,2,2,3]

        for (int i = 1; i < nums.length; i++) {
            if (index == 1 || nums[i] != nums[index - 2]) {
                nums[index] = nums[i];
                index++;
            }
        }
        return index;
    }
}