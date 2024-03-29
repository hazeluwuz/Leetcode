/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */

/**
 * @param {TreeNode} root
 * @param {TreeNode} p
 * @param {TreeNode} q
 * @return {TreeNode}
 */
const lowestCommonAncestor = (root, p, q) => {
  while (root) {
    if (root.val > q.val && root.val > p.val) {
      root = root.left;
    } else if (root.val < q.val && root.val < p.val) {
      root = root.right;    
    } else {
      break;
    }
  }
    return root
};
