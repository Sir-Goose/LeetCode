/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func maxDepth(root *TreeNode) int {
    return dfs(root)
}

func dfs(root *TreeNode) int{
    if root == nil {
        return 0
    }

    leftDepth := dfs(root.Left)
    rightDepth := dfs(root.Right)

    if leftDepth > rightDepth {
        return leftDepth + 1
    }
    return rightDepth + 1

}
