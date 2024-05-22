func partition(s string) [][]string {
    result := [][]string{}
    helper(&result, []string{}, s, 0)
    return result
}

func helper(result *[][]string, current []string, s string, start int) {
    if start == len(s) {
        *result = append(*result, append([]string{}, current...))
        return
    }
    for i := start; i < len(s); i++ {
        if isPalindrome(s, start, i) {
            helper(result, append(current, s[start:i+1]), s, i+1)
        }
    }
}

func isPalindrome(s string, start int, end int) bool {
    for start < end {
        if s[start] != s[end] {
            return false
        }
        start++
        end--
    }
    return true
}

