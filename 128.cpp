class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        unordered_set<int> s(nums.begin(), nums.end());
        int ans = 0;
        for(int i = 0; i < nums.size(); i++){
            
            if(s.find(nums[i]-1) == s.end()){
                int l = 1;
                int x = nums[i];
                while(s.find(x+1) != s.end() ){
                    x++;
                    l++;
                }
                if(l > ans)ans = l;
            }
        }
        return ans;
    }
};
