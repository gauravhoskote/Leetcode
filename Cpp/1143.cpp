class Solution {
public:
    int longestCommonSubsequence(string text1, string text2) {
        vector<vector<int>> arr(text1.length(), vector<int>(text2.length(), 0));
        for(int i = 0; i < text1.length(); i++){
            if(text1[i] == text2[0] || (i != 0 && arr[i-1][0] == 1)){arr[i][0] = 1;}
        }
        for(int j = 0; j < text2.length(); j++){
            if(text1[0] == text2[j] || (j != 0 && arr[0][j-1] == 1)){arr[0][j] = 1;}
        }
        for(int i = 1; i < text1.length(); i++){
            for(int j = 1; j < text2.length(); j++){
                if(text1[i] == text2[j]){
                    arr[i][j] = arr[i-1][j-1]+1;
                }else{
                    arr[i][j] = max(arr[i-1][j], arr[i][j-1]);
                }
            }
        }
        return arr.back().back();
    }
};
