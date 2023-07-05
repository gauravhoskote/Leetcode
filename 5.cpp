class Solution {
public:

    string longestPalindrome(string s) {
        pair<int,int> p = {0,0};
        vector<vector<int>> arr(s.length(), vector<int>(s.length(), 0));
        for(int i = 0; i < s.length(); i++){
            for(int j = 0; j <= i; j++){
                arr[i][j] = 1;
            }
        }
        for(int j = 1; j < s.length(); j++){
            int ii = 0;
            int jj = j;
            while(jj < s.length()){
                if(s[ii] == s[jj]){
                    arr[ii][jj] = arr[ii+1][jj-1];
                }
                if(arr[ii][jj] == 1 && abs(jj-ii) > abs(p.second - p.first)){
                    p.second = jj;
                    p.first = ii;
                }
                jj++;
                ii++;
            }
        }
        string sol = "";
        for(int i = p.first; i <= p.second; i++){
            sol = sol + s[i];
        }
        return sol;
    }
};
