func maxScoreWords(words []string, letters []byte, score []int) int {
    count := make([]int, 26)
    for _, c := range letters {
        count[c-'a']++
    }

    return backtrack(words, count, score, 0)
}

func backtrack(words []string, count []int, score []int, index int) int {
    if index == len(words) {
        return 0
    }

    maxScore := backtrack(words, count, score, index+1)

    wordScore := 0
    canUse := true
    for _, c := range words[index] {
        count[c-'a']--
        if count[c-'a'] < 0 {
            canUse = false
        }
        wordScore += score[c-'a']
    }

    if canUse {
        maxScore = max(maxScore, wordScore+backtrack(words, count, score, index+1))
    }

    for _, c := range words[index] {
        count[c-'a']++
    }

    return maxScore
}

func max(a, b int) int {
    if a > b {
        return a
    }
    return b
}
