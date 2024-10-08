public class Solution {
    public double MinimumAverage(int[] nums) {
        List<double> averages = new List<double>();
        List<int> numbers = new List<int>(nums);
        numbers.Sort();
        while (numbers.Count> 0)
        {
            double small = numbers[0];
            double large = numbers[numbers.Count - 1];
            numbers.RemoveAt(0);
            numbers.RemoveAt(numbers.Count- 1);

            averages.Add((small + large) / 2);
        }
        return averages.Min();
    }
}
