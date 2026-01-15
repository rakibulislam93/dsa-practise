class Solution {
public:
    vector<int> diStringMatch(string s) {
        int low = 0;
        int high = s.size();
        vector<int>result;
        for(char c : s){
            if(c=='I'){
                result.push_back(low);
                low += 1;
            }
            else{
                result.push_back(high);
                high -= 1;
            }
        }
        result.push_back(low);

        return result;
    }
};