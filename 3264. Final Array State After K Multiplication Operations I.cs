public class Solution {
    public int[] GetFinalState(int[] nums, int k, int multiplier) {
        for (int i = 0; i < k; i++)
        {
            int minimum = nums.Min();
            int pos = Array.IndexOf(nums, minimum);
            nums[pos] = minimum * multiplier;
        }
        return nums;
    }
}
