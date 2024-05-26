func containsDuplicate(nums []int) bool {
    uniques := make(map[int]int)
    for i := 0; i < len(nums); i++ {
        _, ok := uniques[nums[i]]
        if ok {
            uniques[nums[i]] += 1
        } else {
            uniques[nums[i]] = 1
        }
    }
    for _, val := range uniques {
        if val != 1 {
            return true
        }
    }
    return false
}

