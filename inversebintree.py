# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None
        else:
            root.left, root.right = self.invertTree(root.right), self.invertTree(
                root.left
            )
            return root


# Compare this snippet from New folder\codePractice\longestpalindromicsubstring.py:
# class Solution:
#     def longestPalindrome(self, s: str) -> str:
#         if len(s) == 1:
#             return s
#         if len(s) == 2:
#             if s[0] == s[1]:
#                 return s
#             else:
#                 return s[0]
#         if len(s) == 3:
#             if s[0] == s[2]:
#                 return s
#             else:
#                 return s[1]
#         if len(s) == 4:
#             if s[0] == s[3] and s[1] == s[2]:
#                 return s
#             elif s[0] == s[2] and s[1] == s[3]:
#                 return s[0:3]
#             elif s[0] == s[1] and s[2] == s[3]:
#                 return s[1:4]
#             else:
#                 return s[1]
#         if len(s) == 5:
