class Solution {
public:

    int f(int i, vector<int>& nums, vector<int>& dp){
        if(i < 0)return 0;
        if(dp[i] != -1)return dp[i];
        return dp[i] = max(nums[i]+f(i-2, nums, dp), max(f(i-2, nums, dp), f(i-1, nums, dp)) );
    }

    int rob(vector<int>& nums) {
        vector<int> dp(nums.size(), -1);
        return max(f(nums.size()-1, nums, dp), f(nums.size()-2, nums, dp));
    }
};
