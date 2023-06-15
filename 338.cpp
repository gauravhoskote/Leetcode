class Solution {
private:
    int ones(int n){
        int ans = 0;
        while(n){
            ans = ans + (n%2);
            n = n / 2;
        }
        return ans;
    }
public:
    vector<int> countBits(int n) {
        vector<int> ans;
        for(int i = 0; i <= n; i++){
            ans.push_back(ones(i));
        }
        return ans;
    }
};
