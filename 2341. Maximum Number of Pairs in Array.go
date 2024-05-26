func numberOfPairs(nums []int) []int {
    output := []int{0, 0}
    elements := make(map[int]int)
    for i := 0; i < len(nums); i++ {
        _, ok := elements[nums[i]]

        if ok {
            elements[nums[i]] += 1
        } else {
            elements[nums[i]] = 1
        }
    }
    count := 0
    for _, value := range elements {
        if value % 2 != 0 {
            count++
        }
    }
    output[0] = (len(nums) - count) / 2
    output[1] = count
    return output
}
