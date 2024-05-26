func twoOutOfThree(nums1 []int, nums2 []int, nums3 []int) []int {
    var output []int
    values := make(map[int]int)
    distinct1 := make(map[int]int)
    distinct2 := make(map[int]int)
    distinct3 := make(map[int]int)

    for i := 0; i < len(nums1); i++ {
        distinct1[nums1[i]] = nums1[i]
    }

    for i := 0; i < len(nums2); i++ {
        distinct2[nums2[i]] = nums2[i]
    }

    for i := 0; i < len(nums3); i++ {
        distinct3[nums3[i]] = nums3[i]
    }

    for key, _ := range distinct1 {
        _, ok := values[key] 
        if ok {
            values[key] += 1
        } else {
            values[key] = 1
        }

    }

    for key, _ := range distinct2 {
        _, ok := values[key] 
        if ok {
            values[key] += 1
        } else {
            values[key] = 1
        }

    }

    for key, _ := range distinct3 {
        _, ok := values[key] 
        if ok {
            values[key] += 1
        } else {
            values[key] = 1
        }

    }


    for key, value := range values {
        if value > 1 {
            output = append(output, key)
        }
    }

    return output

}
