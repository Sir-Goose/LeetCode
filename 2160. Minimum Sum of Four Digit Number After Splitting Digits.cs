public class Solution {
    public int MinimumSum(int num) {
        string stringNum = num.ToString();
        char[] charArray = stringNum.ToCharArray();
        Array.Sort(charArray);
        string sortedStringNum = new string(charArray);
        string num1 = $"{sortedStringNum[0]}{sortedStringNum[2]}";
        string num2 = $"{sortedStringNum[1]}{sortedStringNum[3]}";

        return int.Parse(num1) + int.Parse(num2);
    }
}
