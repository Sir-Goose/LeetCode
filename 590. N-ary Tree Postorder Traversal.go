/**
 * Definition for a Node.
 * type Node struct {
 *     Val int
 *     Children []*Node
 * }
 */

func postorder(root *Node) []int {
    var result []int
    var helper func(*Node)
    helper = func(node *Node) {
        if node == nil {
            return
        }
        for _, child := range node.Children {
            helper(child)
        }
        result = append(result, node.Val)
    }
    helper(root)
    return result
}
