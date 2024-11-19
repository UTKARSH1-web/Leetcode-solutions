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
    vector<vector<int>> zigzagLevelOrder(TreeNode* root) {
        vector<vector<int>> res;
    if (!root)
        return res;
    queue<TreeNode*> q;
    q.push(root);
    int f =1;
    while (!q.empty()) {
        int levelSize = q.size(); 
        vector<int> lev;
        for (int i = 0; i < levelSize; i++) {
            TreeNode* curr = q.front();
            q.pop();
            lev.push_back(curr->val);
            if (curr->left)
                q.push(curr->left);
            if (curr->right)
                q.push(curr->right);
        }
        if (f)
            res.push_back(lev);
        else{
            reverse(lev.begin(),lev.end());
            res.push_back(lev);
        }
        f = f^1;
    }
    return res;
    }
};