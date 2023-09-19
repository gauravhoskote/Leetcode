class Solution {
public:
    int eraseOverlapIntervals(vector<vector<int>>& intervals) {
        int ans = 0;
        int n = intervals.size();
        int i = 0;
        sort(intervals.begin(), intervals.end());
        while(i < n-1){
            if(intervals[i][1] > intervals[i+1][0]){
                if(intervals[i][1] < intervals[i+1][1]){
                    intervals[i+1] = intervals[i];
                }
                ans++;
            }
            i++;
        }
        return ans;
    }
};
