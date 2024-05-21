func buildArray(target []int, n int) []string {
    var output []string

    j := 0
    for i := 1; i <= n; i++ {
        if i == target[j] {
            fmt.Println(i)
            fmt.Println(target[j])
            output = append(output, "Push")
            if j+1 < len(target) {
                j += 1
            } else {
                return output
            }
        } else {
            output = append(output, "Push")
            output = append(output, "Pop")
        }

    }

    return output
    }

