public class Solution {
    public int MinSwaps(string s) {
        int output = 0;
        int balance = 0;
        char[] charArray = s.ToCharArray();
        int lastOpen = charArray.Length - 1;
        for (int i = 0; i < charArray.Length; i++)
        {
            if (charArray[i] == '[')
            {
                balance--;
            }
            else
            {
                balance++;
            }
            if (balance > 0)
            {
                // swap
                charArray[i] = '[';
                // look for end opening bracket
                for (int j = lastOpen; j > i; j--)
                {
                    if (charArray[j] == '[')
                    {
                        lastOpen = j;
                        charArray[j] = ']';
                        balance -= 2;
                        output++;
                        break;
                    }
                }
             }
        }
        return output;
    }
}
