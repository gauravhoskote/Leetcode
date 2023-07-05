class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int x = nums[0];
        int sol = INT_MIN;
        for(int i = 1; i < nums.size(); i++){
            sol = max(sol, x);
            x = max(nums[i], x + nums[i]);
        }
        sol = max(sol, x);
        return sol;
    }
};
