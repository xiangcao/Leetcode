class Solution {
    //my own solution.  time is optimal but code is not. see solution 3
    public void moveZeroes(int[] nums) {
        int firstZero = -1;
        for (int i=0; i< nums.length; i++){
            if (nums[i] == 0) {
                if (firstZero == -1){
                    firstZero = i ;
                }
            }
            if (nums[i] != 0) {
                if(firstZero == -1) {
                    continue;
                }
                swap(nums, i, firstZero);
                firstZero += 1;
            }
        }
    }
    public void swap(int[] nums, int i, int j){
        int temp = nums[i];
        nums[i] = nums[j];
        nums[j] = temp;
    }
    
    # sol 2
    public void moveZeroes(int[] nums) {
        int j = 0;
        for(int i = 0; i < nums.length; i++) {
            if(nums[i] != 0) {
                int temp = nums[j];
                nums[j] = nums[i];
                nums[i] = temp;
                j++;
            }
        }
    }

    # sol 3
    public void moveZeroes(int[] nums) {
        int leftMostZeroIndex = 0; // The index of the leftmost zero
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] != 0) {
                if (i > leftMostZeroIndex) { // There are zero(s) on the left side of the current non-zero number, swap!
                    nums[leftMostZeroIndex] = nums[i];
                    nums[i] = 0;
                }

                leftMostZeroIndex++;
            }
        }
    }
    
    void moveZeroes(vector<int>& nums) {
        int lastNonZeroFoundAt = 0;
        // If the current element is not 0, then we need to
        // append it just in front of last non 0 element we found. 
        for (int i = 0; i < nums.size(); i++) {
            if (nums[i] != 0) {
                nums[lastNonZeroFoundAt++] = nums[i];
            }
        }
        // After we have finished processing new elements,
        // all the non-zero elements are already at beginning of array.
        // We just need to fill remaining array with 0's.
        for (int i = lastNonZeroFoundAt; i < nums.size(); i++) {
            nums[i] = 0;
        }
    }
    
    void moveZeroes(vector<int>& nums) {
        int idx = 0;
        for (int i = 0; i < nums.size(); ++i) {
            if (nums[i] != 0) {
                nums[idx] = nums[i];
                if (idx < i)
                    nums[i] = 0;
                ++idx;
            }
        }
    }
};
}
