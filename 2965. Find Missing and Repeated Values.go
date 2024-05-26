func findMissingAndRepeatedValues(grid [][]int) []int {
    output := []int{0, 0}
    var nums [] int
    for i := 0; i < len(grid); i++ {
        for j := 0; j < len(grid); j++ {
            nums = append(nums, grid[i][j])
        }
    }

    sort.Ints(nums)
    fmt.Println(nums)
    elements := make(map[int]int)
    for i := 0; i < len(nums); i++ {
        _, ok := elements[nums[i]]
        if ok {
            output[0] = nums[i]
            elements[nums[i]] += 1
        } else {
            elements[nums[i]] = 1
        }
    }
	var keys []int

	for key := range elements{
		keys = append(keys, key)
	}
    fmt.Println(elements)

    sort.Ints(keys)
    fmt.Println(keys)
    n := len(grid)
    for i := 1; i <= n * n; i++ {
        _, ok := elements[i]
        if !ok {
            output[1] = i
        }
    } 



    return output
}
