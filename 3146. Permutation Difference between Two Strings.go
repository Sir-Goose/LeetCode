func findPermutationDifference(s string, t string) int {
    totalDifference := 0
    
    for i := 0; i < len(s); i++ {
        for j := 0; j < len(t); j++ {
            if s[i] == t[j] {
                difference := i - j
                if difference < 0 {
                    difference *= -1
                }
                totalDifference += difference

            }
        }
    }
    return totalDifference
}
