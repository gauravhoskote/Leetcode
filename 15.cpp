class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        sort(nums.begin(),nums.end());
        vector<vector<int>> ans;
        set<vector<int>> s;
        for(int i = 0; i < nums.size()-2; i++){
            int j = i+1;
            int k = nums.size()-1;
            while(j < k){
                if(nums[i]+ nums[j]+ nums[k] == 0){
                    if(s.find({nums[i], nums[j], nums[k]}) == s.end()){
                        ans.push_back({nums[i], nums[j], nums[k]});
                        s.insert({nums[i], nums[j], nums[k]});
                    }
                    j++;
                }else if(nums[i]+ nums[j]+ nums[k] < 0){
                    j++;
                }else{
                    k--;
                }
            }
        }
        return ans;
        
    }
};
