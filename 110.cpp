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

    int depth(TreeNode* root){
        if(root == NULL)return 0;
        return 1 + max(depth(root->left), depth(root->right));
    }

    bool isBalanced(TreeNode* root) {
        if(root == NULL)return true;
        bool b1,b2;
        if(abs( depth(root->left)  - depth(root->right)) <= 1 ){
            b1 = isBalanced(root->left);
            b2 = isBalanced(root->right);
        }else{
            return false;
        }
        return b1 && b2;
    }
};
