class Solution {
public:

    int f(string w1, string w2, int i, int j,  vector<vector<int>>& dp){
        if(dp[i][j] != -1)return dp[i][j];
        if(i == w1.length() && j == w2.length()){
            return 0;
        }else if(i == w1.length()){
            return dp[i][j] = 1 + f(w1,w2,i,j+1, dp);
        }else if(j == w2.length()){
            return dp[i][j] = 1 + f(w1,w2,i+1,j, dp);
        }else{
            int x1 = 1 + min( min(f(w1,w2,i+1,j, dp), f(w1,w2,i, j+1, dp)), f(w1,w2,i+1,j+1, dp) );
            int x2 = INT_MAX;
            if(w1[i] == w2[j]) x2 = f(w1,w2,i+1,j+1, dp);
            return dp[i][j] = min(x1,x2);
        }

    }

    int minDistance(string word1, string word2) {
        vector<vector<int>> dp(word1.length()+1, vector<int>(word2.length()+1, -1));
        return f(word1, word2, 0,0, dp);
    }
};
