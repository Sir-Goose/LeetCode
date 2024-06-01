func scoreOfString(s string) int {
    values := make([]int, 0) 
    score := 0

    for i := 0; i < len(s); i++ {
        values = append(values, int(byte(s[i])))
    }
    for j := 0; j < len(values) - 1; j++ {
        score += abs(values[j] - values[j + 1])
    }
    return score
}

func abs(numIn int) int {
    if numIn < 0 {
        numIn *= -1
    }
    return numIn

}

