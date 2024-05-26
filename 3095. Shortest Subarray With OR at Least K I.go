func minimumSubarrayLength(nums []int, k int) int {
    n := len(nums)
    
    for i := 0; i < n; i++ {
        if nums[i] >= k {
            return 1
        }
    }
    
    for i := 2; i <= n; i++ {
        for j := 0; j <= n-i; j++ {
            OR := check(nums[j : j+i])
            if OR >= k {
                return i
            }
        }
    }
    
    return -1
}

func check(elements []int) int {
    OR := elements[0]
    for i := 1; i < len(elements); i++ {
        OR |= elements[i]
    }
    return OR
}
