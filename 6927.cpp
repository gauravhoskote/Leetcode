class Solution {
public:
    int minimumIndex(vector<int>& nums) {
        int hfe = -1;
        int hf = 0;
        map<int,int> m;
        vector<vector<pair<int,int>>> d(2, vector<pair<int,int>>(nums.size(), {-1,-1}));
        for(int i = 0; i < nums.size(); i++){
            m[nums[i]]++;
            if(hf < m[nums[i]]){
                hf = m[nums[i]];
                hfe = nums[i];
            }
            d[0][i].first = hf;
            d[0][i].second = hfe;
        }
        hfe = -1;
        hf = 0;
        map<int,int> mm;
        
        for(int i = nums.size()-1; i >= 0; i--){
            mm[nums[i]]++;
            if(hf < mm[nums[i]]){
                hf = mm[nums[i]];
                hfe = nums[i];
            }
            d[1][i].first = hf;
            d[1][i].second = hfe;
        }
        for(int i = 0; i < nums.size()-1; i++){
            if(d[0][i].second == d[1][i+1].second && (d[0][i].first * 2) > (i+1) && (d[1][i+1].first * 2) > (nums.size() - (i+1)) ){
                return i;
            }
        }
        return -1;
    }
};
