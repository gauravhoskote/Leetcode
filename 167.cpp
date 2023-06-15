class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        for(int i= 0; i < numbers.size()-1; i++){
            if(binary_search(numbers.begin()+i+1, numbers.end(), target - numbers[i])){
                return {i+1,(int)(lower_bound(numbers.begin()+i+1, numbers.end(), target - numbers[i]) - numbers.begin())+1};
            }
        }
        return {0,0};
    }
};
