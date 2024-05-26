func arithmeticTriplets(nums []int, diff int) int {
    count := 0
    for i := 0; i < len(nums); i++ {
        for j := i; j < len(nums); j++ {
            for k := j; k < len(nums); k++ {
                if i < j && j < k {
                    if nums[j]-nums[i] == diff && nums[k]-nums[j] == diff {
                        count++
                    }
                }
            }
        }
    }
    return count
}
