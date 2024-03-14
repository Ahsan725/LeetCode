class Solution {
    public void merge(int[] nums1, int m, int[] nums2, int n) {
        //non decreasing order -> 7 8 9 10 ascending order
        //stored the sorted array inside nums1 array
        //so instead of length we will have to use m to find out the elements

        //approach: start a for loop where the comparisons are made from
        //each array and then the smaller one is added and the next one 
        //is checked the next time. 


        int i = m - 1;
        int j = n - 1;
        int k = m + n - 1;
        
        //nums1[1,2,4,0,0,0] i = 1
        //nums2[3,5,6] j = 0
        // k = 3

        while (j >= 0) { //while nums2 has elements
            if (i >= 0 && nums1[i] > nums2[j]) { //if nums1 has elements and if nums1 > nums2
                nums1[k] = nums1[i]; //add at the last index since we are filling it up from end
                k--; //move up an index
                i--; //move up an index on nums1 since we added one
            } else {
                nums1[k] = nums2[j]; //if nums2 was bigger add that instead
                k--; //move up an index
                j--; //move up an index
            }
        }
    }
}
