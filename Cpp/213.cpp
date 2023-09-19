class Solution {
public:

     int f(int i, vector<int>& nums, vector<int>& dp){
        if(i < 0)return 0;
        if(dp[i] != -1)return dp[i];
        return dp[i] = max(nums[i]+f(i-2, nums, dp), max(f(i-2, nums, dp), f(i-1, nums, dp)) );
    }

    int rob(vector<int>& nums) {
        if(nums.size() == 1)return nums[0];
        vector<int> dp1(nums.size(), -1);
        int res1 =  f(nums.size()-2, nums, dp1);
        reverse(nums.begin(), nums.end());
        nums.pop_back();
        vector<int> dp2(nums.size(), -1);
        int res2 = f(nums.size()-1, nums, dp2);
        return max(res1, res2);
    }
};
