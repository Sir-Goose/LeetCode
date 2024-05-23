func beautifulSubsets(nums []int, k int) int {
    // get superset 
    // check if beautiful
    count := 0
    superset := generateSubsets(nums)
    for i := 0; i < len(superset); i++ {
        if len(superset[i]) != 0 {
            if isBeautiful(superset[i], k) {
                count++
            }
        }
    }
    return count
}

func isBeautiful(set []int, k int) bool {
    for i := 0; i < len(set); i++ {
        for j := 0; j < len(set); j++ {
            if abs(set[i] - set[j]) == k {
                return false
            }
        }
    }
    return true
}

func abs(input int) int {
    if input < 0 {
        input *= -1
    }
    return input
}




func generateSubsets(nums []int) [][]int {
	n := len(nums)
	totalSubsets := 1 << n 
	subsets := make([][]int, 0, totalSubsets)

	for i := 0; i < totalSubsets; i++ {
		subset := []int{}
		for j := 0; j < n; j++ {
			if i&(1<<j) != 0 {
				subset = append(subset, nums[j])
			}
		}
		subsets = append(subsets, subset)
	}

	return subsets
}

