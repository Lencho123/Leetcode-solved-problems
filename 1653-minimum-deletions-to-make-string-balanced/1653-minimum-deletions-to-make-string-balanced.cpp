class Solution {
public:
    int minimumDeletions(string s) {
        int n = s.size();
        vector<int> post_a(n,0);
        vector<int> pre_b(n,0);
        int res = INT_MAX;

        for (int i = 1; i<n; i++){
            int b = (s[i - 1] == 'b');
            int a = (s[n - i] == 'a');


            pre_b[i]+=b + pre_b[i-1];
            post_a[n-i-1]+=a + post_a[n-i];

        }

        for (int i = 0; i<n; i++){
            res = min(res,pre_b[i]+post_a[i]);
        }

    
        return res;
        
    }
};
