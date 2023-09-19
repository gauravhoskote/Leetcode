class Solution {
public:
    int sumOfSquares(vector<int>& nums) {
        int n = nums.size();
        int sol = 0;
        for(int i = 0; i < nums.size(); i++){
            if(n%(i+1) == 0){
                sol += pow(nums[i],2);
            }
        }
        return sol;
        
    }
};
