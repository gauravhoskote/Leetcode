class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        int n = matrix.size() * matrix[0].size();
        int rit = n-1;
        int left= 0;
        int m = 0;
        int i = (m / matrix[0].size());
        int j = (m % matrix[0].size());
        while(left <= rit){
            m = left + (rit - left)/2;
            i = (m / matrix[0].size());
            j = (m % matrix[0].size());
            if(matrix[i][j] == target){
                return true;
            }else if(matrix[i][j] > target){
                rit = m-1;
            }else{
                left = m + 1;
            }
        }
        return false;
    }
};
