class Solution {
public:
    bool checkInclusion(string s1, string s2) {
        if(s1.length() > s2.length()){
            return false;
        }
        unordered_map<char, int> m;
        for(int i = 0; i < s1.length(); i++){
            m[s1[i]]++;
        }
        unordered_map<char, int> t;
        for(int i = 0; i < s1.length(); i++){
            t[s2[i]]++;
        }
        
        if(s1.length() == s2.length()){
            return m == t;
        }
        for(int i = s1.length(); i < s2.length(); i++){
            if(m == t)return true;
            t[s2[i]]++;
            t[s2[i-s1.length()]]--;
            if(t[s2[i-s1.length()]] == 0){
                t.erase(t.find(s2[i-s1.length()]));
            }
        }
        if(m == t)return true;
        return false;
    }
};
