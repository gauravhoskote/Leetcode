/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    int maxPathSum(TreeNode* root) {
        int mm = root->val;
        f(root,mm);
        return mm;
    }

    int f(TreeNode* root, int& mm){
        if(root == NULL){
            return 0;
        }
        int lc = max(f(root->left, mm),0);
        int rc = max(f(root->right, mm),0);

        mm = max(mm, lc+rc+root->val);

        return root->val + max(lc,rc);
    }

};
