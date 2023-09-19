class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        vector<int> ans;
        unordered_map<int,int> m;
        for(int i = 0; i < nums.size(); i++){
            m[nums[i]]++;
        }
        vector<vector<int>> x(nums.size()+1);
        for(auto it = m.begin(); it != m.end(); it++){
            x[it->second].push_back(it->first);
        }
        int ctr=0;
        
        for(int i = x.size()-1; i >= 0; i--){
            if(ctr >= k)break;
            for(int j = 0; j < x[i].size(); j++){
                ans.push_back(x[i][j]);
                ctr++;
            }
        }
         return ans;
        
    }
};
