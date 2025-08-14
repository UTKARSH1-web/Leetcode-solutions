class Solution {
public:
    void comb(int i,int n , int k, vector<vector<int>> &l,vector<int> &c){
        if (c.size()==k){
            l.push_back(c);
            return;
        }
        for (int j=i; j<=n;j++){
            c.push_back(j);
            comb(j+1,n,k,l,c);
            c.pop_back();
        }
    }
    vector<vector<int>> combine(int n, int k) {
        vector<int> c;
        vector<vector<int>> l;
        int i =1;
        comb(i,n,k,l,c);
        return l;
    }
};