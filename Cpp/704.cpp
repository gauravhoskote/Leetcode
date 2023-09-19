class Solution {
public:
    int search(vector<int>& nums, int target) {
        long long int left = 0, rit = nums.size()-1;
        long long int mid=0;
        while(left <= rit){
            mid = left + (rit-left)/2;
            if(nums[mid] == target){
                return mid;
            }else if(nums[mid] > target){
                rit = mid-1;
            }else{
                left = mid+1;
            }
        }
        return -1;
    }
};
