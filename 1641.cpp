class Solution {
public:
    int countVowelStrings(int n) {
        vector<int> arr(5, 1);
        for(int i = 0; i < n-1; i++){
            for(int j = 1; j < 5; j++){
                arr[j] += arr[j-1]; 
            }
        }
        int ans = 0;
        for(int j = 0; j < 5; j++){
            ans += arr[j];
        }
        return ans;
    }
};
