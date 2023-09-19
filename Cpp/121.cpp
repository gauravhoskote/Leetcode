class Solution {
public:
    int maxProfit(vector<int>& prices) {
        if(prices.size() == 0 || prices.size() == 1)return 0;
        int mm = prices[0];
        int sol = 0;
        for(int i = 1; i < prices.size(); i++){
            sol = max(sol, prices[i]-mm);
            mm = min(mm, prices[i]);
        }
        return sol;
    }
};
