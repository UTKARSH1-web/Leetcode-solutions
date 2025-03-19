class Solution {
public:
    double findMaxAverage(vector<int>& nums, int k) {
        double ans=-INT_MAX,sum=0;
        int i=0;
        for (int j=0;j<nums.size();j++){
            sum+=nums[j];
            if (j-i+1==k){
                ans = max(ans,sum/k);
                sum-=nums[i];
                i++;
            }
        }
        return ans;
    }
};