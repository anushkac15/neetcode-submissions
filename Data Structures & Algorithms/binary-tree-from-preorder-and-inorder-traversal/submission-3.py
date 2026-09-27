class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        def solve(start, end):
            if start > end:
                return None

            rootVal = preorder[idx[0]]
            idx[0] += 1

            i = pos[rootVal]

            root = TreeNode(rootVal)

            root.left = solve(start, i - 1)
            root.right = solve(i + 1, end)

            return root

        n = len(preorder)
        idx = [0]

        pos = {}
        for i in range(n):
            pos[inorder[i]] = i

        return solve(0, n - 1)