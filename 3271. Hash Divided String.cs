public class Solution {
    public string StringHash(string s, int k) {
        string result = "";
        List<string> substrings = new List<string>();
        int num_substrings = s.Length / k;
        for (int i = 0; i < num_substrings; i++)
        {
            string substring = "";
            for (int j = 0; j < k; j++)
            {
                substring = substring + s[j];
            }
            s = s.Substring(k);
            substrings.Add(substring);
        }
        foreach (string substring in substrings)
        {
            int hash_sum = 0;
            foreach (char letter in substring)
            {
                hash_sum += ((int)letter - 97);
            }
            int remainder = hash_sum % 26;
            char alphabet_remainder = (char)(remainder+97);
            result += alphabet_remainder;
            //Console.WriteLine(substring);
        }
        return result;
    }
}
