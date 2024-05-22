func numberOfSpecialChars(word string) int {
    chars := map[int]bool{}
    count := 0

    for i := 0; i < len(word); i++ {
        chars[int(word[i])] = true
    }

    for key, _ := range chars {
        key -= 32
        _, ok := chars[key]
        if ok {
            count++
        }
    }
    return count
}

