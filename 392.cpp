class Solution {
public:
    bool isSubsequence(string s, string t) {
        vector<vector<bool>> arr(s.length(), vector<bool>(t.length(), false));
        if(s.length() == 0 )return true;
        if(t.length() == 0)return false;
        arr[0][0] = s[0] == t[0];
        for(int i = 1; i < t.length(); i++){
            arr[0][i] = arr[0][i-1] || (s[0] == t[i]);
        }
        for(int i = 1; i < s.length(); i++){
            for(int j = i; j < t.length(); j++){
                if(s[i] == t[j]){
                    arr[i][j] = arr[i-1][j-1] || arr[i][j-1];
                }else{
                    arr[i][j] = arr[i][j-1];
                }
            }
        }

        return arr.back().back();
    }
};
