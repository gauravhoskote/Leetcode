class Solution {
public:
    int jump(vector<int>& nums) {
        vector<int> arr(nums.size(), INT_MAX);
        arr[0] = 1;
        for(int i = 0; i < nums.size(); i++){
            for(int j =1; j <= nums[i] && i+j < arr.size(); j++){
                arr[i+j] = min(arr[i+j], arr[i]+1);
            }
        }
        return arr.back()-1;
    }
};
