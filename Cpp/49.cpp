class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        vector<vector<string>> sol;
        map<map<char, int>, vector<string>> m;
        for(int i = 0; i < strs.size(); i++){
            map<char, int> mm;
            for(auto el : strs[i]){
                mm[el]++;
            }
            m[mm].push_back(strs[i]);
        }
        for(auto it = m.begin(); it != m.end(); it++){
            sol.push_back(it->second);
        }
        return sol;
    }
};
