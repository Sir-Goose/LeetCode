public class Solution {
    public int CountKConstraintSubstrings(string s, int k) {
        int output = 0;
        // expanding sliding window
        for (int i = 1; i <= s.Length; i++)
        {
            int windowLength = i;
            // j starting position
            for (int j = 0; j+i <= s.Length; j++)
            {
                Console.WriteLine($"i: {i}, j: {j} j+i: {j+i}");
                string substring = s.Substring(j, i);
                Console.WriteLine($"Substring: {substring}");
                // count 0 and 1s
                int zeroCount = 0;
                int oneCount = 0;
                foreach (char character in substring)
                {
                    if (character == '1')
                    {
                        oneCount++;
                    }
                    else 
                    {
                        zeroCount++;
                    }
                }
                if (oneCount <= k || zeroCount <= k)
                {
                    output++;
                }
            }
        }
        return output;
    }
}
