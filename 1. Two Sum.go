func twoSum(nums []int, target int) []int {
    output := make([]int, 2)
    for i := 0; i < len(nums); i++ {
        for j := i+1; j < len(nums); j++ {
            if nums[i] + nums[j] == target {
                output[0] = i
                output[1] = j
            }
        }
    } 
    return output
}

