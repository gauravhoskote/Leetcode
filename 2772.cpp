class Solution {
public:
    bool checkArray(vector<int>& nums, int k) {
        int d = 0;
        queue<pair<int, int>> q;
        for(int i = 0; i < nums.size(); i++){
            if(!q.empty()){
                if(q.front().first == i){
                    d = d - q.front().second;
                    q.pop();
                }
            }
            if(nums[i] != d){
                if(nums[i] > d){
                    if(i+k > nums.size())return false;
                    q.push({i+ k, nums[i]-d});
                    d = nums[i];
                }else{
                    return false;
                }
            }
        }
        return true;
    }
};
