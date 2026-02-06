class Solution {
public:
    int minRemoval(vector<int>& nums, int k) {
        int n = nums.size();
        sort(nums.begin(),nums.end());

        int res = INT_MAX;

        int l = 0;
        int r = 0;

        while (r < n){
            if (nums[l]*k >= nums[r]){
                r++;
                res = min(res,l+n-r);
            }else{
                l++;
            }
        }
    return res;
        
    }
};