class Solution {
public:
    int maximumBeauty(vector<int>& nums, int k) {
        vector<pair<int,int>> a;
        for(auto el : nums){
            a.push_back({el-k, el+k});
        }
        vector<pair<int,char>> d;
        for (int i = 0; i < a.size(); i++) {
            d.push_back({ a[i].first, 'x' });
            d.push_back({ a[i].second, 'y' });
        }
        sort(d.begin(), d.end());
        int c = 0;
        int sol = 0;
        for(auto el : d){
            if(el.second == 'x'){
                c++;
            }
            if(el.second == 'y'){
                c--;
            }
            sol = max(sol, c);
            
        }
        return sol;
        
    }
};
