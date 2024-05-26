func findMaxK(nums []int) int {
    big := 0
    for i := 0; i < len(nums); i++ {
        if nums[i] > big {
            for j := 0; j < len(nums); j++ {
                if nums[j] == nums[i] * -1 {
                    big = nums[i]
                }
            }
        }
    }
    if big == 0 {
        return -1
    } else {
        return big
    }
}
