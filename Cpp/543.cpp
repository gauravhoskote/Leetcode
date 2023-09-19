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

    int f(TreeNode* root){
        return root == NULL? 0 : (1 + max(f(root->left), f(root->right)));
    }

    void f1(TreeNode* root, int& sol){
        if(root  == NULL)return;
        sol = max(sol, 1 + f(root->left) + f(root->right));
        f1(root->left, sol);
        f1(root->right, sol);
    }

    int diameterOfBinaryTree(TreeNode* root) {
        if(root == NULL) return 0;
        int sol = 0;
        f1(root, sol);
        return sol-1;
    }
};
