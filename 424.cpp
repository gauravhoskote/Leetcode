class Solution {
public:
    int characterReplacement(string s, int k) {
        int i = 0;
        int j = 0;
        int ans = 0;
        int n = s.length();
        unordered_map<char,int> ss;
        int mc = 0;
        while(j < n){
            ss[s[j]]++;
            mc = max(mc, ss[s[j]]);
            if(j-i + 1 - mc > k){
                ss[s[i]]--;
                i++;
            }
            ans = max(ans, j - i + 1);
            j++;
        }
        return ans;
    }
};
