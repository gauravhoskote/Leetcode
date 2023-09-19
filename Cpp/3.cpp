class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int i = 0, j = 0;
        int n = s.length();
        if(n == 1)return 1;
        map<char, int> m;
        int sol = 0;
        while(j < s.length()){
            if(m[s[j]]>0){
                while(s[i] != s[j]){
                    m[s[i]]--;
                    i++;
                }
                i++;
                j++;
            }else{
                m[s[j]]++;
                j++;
            }
            sol = max(sol, j-i);
        }
        return sol;
    }
};
