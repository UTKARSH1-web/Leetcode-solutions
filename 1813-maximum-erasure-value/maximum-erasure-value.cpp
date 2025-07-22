
class Solution {
public:
    int maximumUniqueSubarray(vector<int>& nums) {
        set<long long int> a;
        long long int i=0,ans=0,j=0,curr=0,n=nums.size();
        while (j<n){
            if (a.find(nums[j])==a.end()){
                a.insert(nums[j]);
                curr+=nums[j];
                ans = max(ans,curr);
                j++;
            }
            else{
                a.erase(nums[i]);
                curr-=nums[i];
                i++;
            }
        }
        return ans;
    }
};