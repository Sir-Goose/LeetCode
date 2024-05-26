func countTriplets(arr []int) int {
    count := 0
    for i := 0; i < len(arr); i++ {
        for j := 0; j < len(arr); j++ {
            for k := 0; k < len(arr); k++ {
                if 0 <= i && i < j && j <= k && k < len(arr) {
                    a := arr[i]
                    for l := i + 1; l < j; l++ {
                        a ^= arr[l]
                    }
                    b := arr[j]
                    for m := j + 1; m <= k; m++ {
                        b ^= arr[m]
                    }
                    if a == b {
                        count++
                    }
                }
            }
        }
    }
    return count
}

