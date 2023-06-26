class Solution {
public:
    vector<int> getRow(int rowIndex) {
        vector<vector<int>> arr(2, vector<int>(rowIndex+1, 1));
        if(rowIndex <= 1)return vector<int>(rowIndex+1, 1);
        for(int i = 2; i <= rowIndex; i++){
            int j = i % 2;
            int jj = 1;
            if(j == 1)jj = 0;
            for(int k = 1; k <= i-1; k++){
                arr[j][k] = arr[jj][k] + arr[jj][k-1];
            }
        }
        return arr[rowIndex%2];
    }
};
