
class Solution {
public:
    void merge(vector<int>& v1, int m, vector<int>& v2, int n) {
        int j=0;
        for(int i=m; i<m+n; i++)
        {
            v1[i]=v2[j];
            j++;
        }
        sort(v1.begin(),v1.end());
    }
};