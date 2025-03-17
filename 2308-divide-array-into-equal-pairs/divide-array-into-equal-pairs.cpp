class Solution {
public:
    bool divideArray(vector<int>& nums) {
        unordered_map<int,int> d;
        for(auto &i:nums){
            d[i]++;
        }
        // bool flag=true;
        for(auto i:d){
            if(i.second%2 !=0)
                return false;
        }
        return true;
    }
};