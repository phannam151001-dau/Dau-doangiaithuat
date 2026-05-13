class Solution:
    def sortedArrayToBST(self, nums):

        def tao_cay(trai, phai):
            if trai > phai:
                return None

            giua = (trai + phai) // 2

            node = TreeNode(nums[giua])

            node.left = tao_cay(trai, giua - 1)
            node.right = tao_cay(giua + 1, phai)

            return node

        return tao_cay(0, len(nums) - 1)