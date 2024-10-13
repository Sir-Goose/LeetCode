public class Solution {
    public int DuplicateNumbersXOR(int[] nums) {
        int result;
        List<int> sortedNums = new List<int>(nums);
        sortedNums.Sort();
        List<int> duoList = new List<int>();
        for (int i = 1; i < sortedNums.Count(); i++)
        {
            if (sortedNums[i] == sortedNums[i-1])
            {
                duoList.Add(sortedNums[i]);
            }
        }
        if (duoList.Count() > 0)
        {
            result = duoList[0];
            for (int i = 1; i < duoList.Count(); i++)
            {
                result = result ^ duoList[i];
            }
            return result;
        }
        else
        {
            return 0;
        }
    }
}
