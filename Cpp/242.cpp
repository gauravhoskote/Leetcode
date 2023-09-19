class Solution {
public:
    bool isAnagram(string s, string t) {
        map<char, int> ms;
        for(auto el : s){
            ms[el]++;
        }
        map<char, int> mt;
        for(auto el : t){
            mt[el]++;
        }
        if(ms.size() != mt.size())return false;
        for(int i = 0; i < ms.size(); i++){
            if(ms[i] != mt[i])return false;
        }
        return true;
    }
};
