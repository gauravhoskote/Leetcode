class Solution {
public:
    int lengthOfLastWord(string s) {
        int ctr = 0;
        int ans = 0;
        for(int i = 0; i < s.length(); i++){
            if(s[i] == ' '){
                if(ctr!= 0)ans = ctr;
                ctr = 0;
            }else{
                ctr++;
            }
        }
        if(ctr != ans && ctr != 0)ans = ctr;
        return ans;
    }
};
