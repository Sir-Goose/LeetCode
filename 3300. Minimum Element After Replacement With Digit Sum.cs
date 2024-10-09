public class Solution {
    public int MinElement(int[] nums) {
        List<int> sums = new List<int>();
        for (int i = 0; i < nums.Length; i++)
        {
            int sum = 0;
            foreach (char digit in nums[i].ToString())
            {
                sum += ((int)digit - 48);
            }
            sums.Add(sum);
        }
        return sums.Min();
    }
}
