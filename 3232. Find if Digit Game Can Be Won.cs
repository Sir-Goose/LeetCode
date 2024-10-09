public class Solution {
    public bool CanAliceWin(int[] nums) {
        int total = nums.Sum();
        int singles = 0;
        foreach (int number in nums)
        {
            if (number > 9)
            {
                singles += number;
            }
        }
        return (total - singles) != singles;
    }
}
