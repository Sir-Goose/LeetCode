func distributeCandies(n int, limit int) int {
    count := 0
    for i := 0; i <= limit && i <= n; i++ {
        for j := 0; j <= limit && i+j <= n; j++ {
            k := n - i - j
            if k <= limit && k >= 0 {
                count++
            }
        }
    }
    return count
}
