class Solution {
public:
    vector<vector<int>> merge(vector<vector<int>>& intervals) {
        sort(intervals.begin(), intervals.end());
        int n = intervals.size();
        int i = 0;
        vector<vector<int>> res;
        while(i < n-1){
            if(intervals[i][1] >= intervals[i+1][0]){
                intervals[i+1][0] = min(intervals[i][0], intervals[i+1][0]);
                intervals[i+1][1] = max(intervals[i][1], intervals[i+1][1]);
            }else{
                res.push_back(intervals[i]);
            }
            i++;
        }
        res.push_back(intervals[i]);
        return res;
    }
};
