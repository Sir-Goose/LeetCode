public class Solution {
    public int MinimumChairs(string s) {
        int count = 0;
        int max = 0;
        foreach (char movement in s)
        {
            if (movement == 'E')
            {
                count++;
            }
            else 
            {
                count--;
            }
            max = Math.Max(count, max);
        }
        return max;
    }
}
