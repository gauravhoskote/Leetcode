class Solution {
public:
    vector<int> spiralOrder(vector<vector<int>>& matrix) {
        int rb = matrix[0].size()-1;
        int lob = matrix.size()-1;
        int lb = 0;
        int ub = 0;
        int dir = 1;
        int ctr = (int)matrix.size() * (int)matrix[0].size();
        vector<int> ans;
        int i=0,j=0;
        while(ctr--){
            ans.push_back(matrix[i][j]);
            switch(dir){
                case 1:
                    if(j == rb){
                        ub++;
                        dir = 2;
                        i++;
                    }else{
                        j++;
                    }
                    break;
                case 2:
                    if(i == lob){
                        rb--;
                        dir = 3;
                        j--;
                    }else{
                        i++;
                    }
                    break;
                case 3:
                    if(j == lb){
                        lob--;
                        dir = 4;
                        i--;
                    }else{
                        j--;
                    }
                    break;
                case 4:
                    if(i == ub){
                        lb++;
                        dir = 1;
                        j++;
                    }else{
                        i--;
                    }
                    break;
            }
        }
        return ans;
        
    }
};
