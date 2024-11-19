class Solution {
public:
    long long maximumSubarraySum(vector<int>& nums, int k) {
        map<int, int> mp;
        long long sum = 0;
        for (int i = 0; i < k; i++) {
            sum += nums[i];
            mp[nums[i]]++;
        }
        long long ans = 0;
        if (mp.size() == k) {
            ans = sum;
        }
        for (int i = k; i < nums.size(); i++) {
            sum += nums[i];
            mp[nums[i]]++;
            sum -= nums[i - k];
            mp[nums[i - k]]--;
            auto it = mp.find(nums[i - k]);
            
            if (it -> second == 0) {
                mp.erase(it);
            }
            if (mp.size() == k) {
                ans = max(ans, sum);
            }
            
        }
        return ans;
    }
};