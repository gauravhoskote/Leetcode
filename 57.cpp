class Solution {
public:
    vector<vector<int>> insert(vector<vector<int>>& intervals, vector<int>& newInterval) {
        int i = 0;
        int n = intervals.size();
        vector<vector<int>> res;
        if(n == 0){
            res.push_back(newInterval);
            return res;
        }
        while(i < n && newInterval[0] > intervals[i][1]){
            res.push_back(intervals[i]);
            i++;
        }
        while(i < n && newInterval[1] >= intervals[i][0]){
            newInterval[0] = min(newInterval[0], intervals[i][0]);
            newInterval[1] = max(newInterval[1], intervals[i][1]);
            i++;
        }
        res.push_back(newInterval);      
        while( i < intervals.size()){
            res.push_back(intervals[i]);
            i++;
        }
        return res;
    }
};
