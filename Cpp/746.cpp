class Solution {
public:
    int f(int i, vector<int>& cost, vector<int>& dp){
        if(i == 0 || i == 1)return cost[i];
        if(dp[i] != -1)return dp[i];
        return dp[i] = (cost[i] + min(f(i-1, cost, dp), f(i-2, cost, dp)));
    }
    int minCostClimbingStairs(vector<int>& cost) {
        vector<int> dp(cost.size(), -1);
        return min(f(cost.size()-1, cost, dp), f(cost.size()-2, cost, dp));
    }
};
