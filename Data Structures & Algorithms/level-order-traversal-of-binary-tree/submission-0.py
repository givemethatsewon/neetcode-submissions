# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result_list: List[List[int]] = []  # 한 레벨을 리스트로 바꿔 저장할 리스트(숫자)
        queue: Deque[Optional[TreeNode]] = deque()

        if root:
            queue.append(root)

        while len(queue) > 0:
            level_list: List[int] = []
            for i in range(len(queue)):
                current: TreeNode = queue.popleft()
                level_list.append(current.val)
                if current.left:
                    queue.append(current.left)
                if current.right:
                    queue.append(current.right)
            result_list.append(level_list)

        return result_list