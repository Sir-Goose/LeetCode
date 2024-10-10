public class Solution {
    public int FinalPositionOfSnake(int n, IList<string> commands) {
        int length = n;
        int pos = 0;
        foreach (string command in commands)
        {
            if  (command == "UP")
            {
                pos -= length;
            }
            if  (command == "DOWN")
            {
                pos += length;
            }
            if  (command == "RIGHT")
            {
                pos += 1;
            }
            if  (command == "LEFT")
            {
                pos -= 1;
            }
        }
        return pos;
    }
}
