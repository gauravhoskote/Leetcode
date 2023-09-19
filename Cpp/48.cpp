class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        map<map<char, int>, vector<string>> m;
        
        for(int i = 0; i < strs.size(); i++){
            map<char,int> charmap;
            for(auto c : strs[i]){
                charmap[c]++;
            }
            m[charmap].push_back(strs[i]);
        }
        
        vector<vector<string>> result;
        for(auto it = m.begin(); it != m.end(); it++){
            result.push_back(it->second);
        }
        return result;

    }
};
