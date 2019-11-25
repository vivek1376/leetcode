#include <bits/stdc++.h>

// https://leetcode.com/problems/binary-tree-level-order-traversal/

using namespace std;


// Definition for a binary tree node.
struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

class Solution {
public:
    vector<vector<int>> levelOrder(TreeNode* root) {
        vector <vector<int>> result;

        queue <TreeNode*> Q;
        queue <int> levels;

        int currlevel = -1, newlevel;

        TreeNode *temp;

        Q.push(root);
        levels.push(0);

        while(!Q.empty()) {
            temp = Q.front();
            Q.pop();

            if (temp == NULL)
                break;

            newlevel = levels.front();
            levels.pop();

            if (newlevel != currlevel) {
                currlevel++;
                result.push_back(vector<int>{});
            }

            result[currlevel].push_back(temp->val);

            if (temp->left) {
                Q.push(temp->left);
                levels.push(currlevel+1);
            }

            if (temp->right) {
                Q.push(temp->right);
                levels.push(currlevel+1);
            }
        }

        return result;
    }
};



