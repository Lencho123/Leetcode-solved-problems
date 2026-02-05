class Solution {
public:
    vector<int> constructTransformedArray(vector<int>& nums) {

    int n = nums.size();
    vector<int> result(n);

    for (int i=0; i < n; i++){
        int ind = ((nums[i]+i)%n+n)%n;
        result[i] = nums[ind];
    }
        
        return result;
    }
};