public class NeighborSum {
    int[][] dgrid;

    public NeighborSum(int[][] grid) {
        dgrid = grid;
    }
    
    public int AdjacentSum(int value) {
        int row;
        int column;
        int n = dgrid[0].Length;
        int sum = 0;
        for (int i = 0; i < this.dgrid.Length; i++) // rows
        {
            for (int j = 0; j < this.dgrid[0].Length; j++) // columns
            {
                if (this.dgrid[i][j] == value)
                {
                    row = i;
                    column = j;
                    // above
                    if (i-1 >= 0)
                    {
                        sum += dgrid[i-1][j];
                    }
                    // below 
                    if (i+1 < n)
                    {
                        sum += dgrid[i+1][j];
                    }
                    // left
                    if (j-1 >= 0)
                    {
                        sum += dgrid[i][j-1];
                    }
                    // right
                    if (j+1 < n)
                    {
                        sum += dgrid[i][j+1];
                    }
                }
            }
        }
        return sum;
    }
    
    public int DiagonalSum(int value) {
        int row;
        int column;
        int n = dgrid[0].Length;
        int sum = 0;
        for (int i = 0; i < this.dgrid.Length; i++) // rows
        {
            for (int j = 0; j < this.dgrid[0].Length; j++) // columns
            {
                if (this.dgrid[i][j] == value)
                {
                    row = i;
                    column = j;
                    // top left
                    if (i-1 >= 0 && j-1 >= 0)
                    {
                        sum += dgrid[i-1][j-1];
                    }
                    // bottom left
                    if (i+1 < n && j-1 >= 0)
                    {
                        sum += dgrid[i+1][j-1];
                    }
                    // top right
                    if (j+1 < n && i-1 >= 0)
                    {
                        sum += dgrid[i-1][j+1];
                    }
                    // bottom right
                    if (j+1 < n && i+1 < n)
                    {
                        sum += dgrid[i+1][j+1];
                    }
                }
            }
        }
        return sum;
    }
}
