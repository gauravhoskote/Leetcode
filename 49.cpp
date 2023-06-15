class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        map< map<char,int> , vector<string> > mm;
        for(int i = 0; i < strs.size(); i++){
            map<char, int> m;
            for(char c : strs[i]){
                m[c]++;
            }
            if(mm.find(m) == mm.end()){
                mm[m] = {strs[i]};
            }else{
                mm[m].push_back(strs[i]);
            }
        }
        vector<vector<string>> ans;
        for(auto it : mm){
            ans.push_back(it.second);
        }
        return ans;
    }
};
