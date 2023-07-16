class Solution {
public:
    int maxProduct(vector<int>& nums) {
        int x = nums[0];
        int maxx = 1;
        int minn = 1;
        int t;
        for(int i = 0; i < nums.size(); i++){
            t = minn;
            minn = min(nums[i], min(nums[i]*minn, maxx * nums[i]));
            maxx = max(nums[i], max(nums[i]*t, maxx * nums[i]));
            x = max(x, maxx);
        }
        return x;
    }
};
