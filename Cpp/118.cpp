class Solution {
public:
    vector<vector<int>> generate(int numRows) {
        vector<vector<int>> arr;//(numRows, vector<int>());
        for(int i = 0; i < numRows; i++){
            arr.push_back(vector<int>(i+1, 0));
            for(int j = 0; j <= i; j++){
                cout<<j<<endl;
                if(j == 0 || i == j){
                    arr[i][j] = 1;
                }
                else{
                    arr[i][j] = (arr[i-1][j]+arr[i-1][j-1]);
                }                
            }
        }
        return arr;
    }
};
