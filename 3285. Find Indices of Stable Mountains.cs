public class Solution {
    public IList<int> StableMountains(int[] height, int threshold) {
        List<int> output = new List<int>();
        for (int i = 1; i < height.Length; i++)
        {
            if (height[i-1] > threshold)
            {
                output.Add(i);
            }
        }
        return output;
    }
}
