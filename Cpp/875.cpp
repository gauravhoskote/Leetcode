class Solution {
public:
    int minEatingSpeed(vector<int>& piles, int h) {
        long long int rit = *max_element(piles.begin(), piles.end());
        long long int left = 1;
        long long int m = 1; // eq to k
        long long int tot = 0;
        long long int sol = INT_MAX;
        while(left <= rit){
            m = left + (rit - left)/2;
            tot = 0;
            for(int i = 0; i < piles.size(); i++){
                tot += piles[i]/m;
                if(piles[i]%m != 0)tot++;
            }
            cout<<"Tot: "<<tot<<endl;
            cout<<"Left: "<<left<<" rit: "<<rit<<" m: "<<m<<endl;
            if(tot > h){
                left = m+1;
            }else{
                rit = m-1;
                sol = min(m,sol);
            }
        }
        return sol;
    }
};
