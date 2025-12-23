
class Solution {
public:
    int subtractProductAndSum(int n) {
        
        int product = 1;
        int total_sum = 0;

        while(n>0){
            int digit = n%10;
            product *= digit;
            total_sum += digit;
            n /=10;
        }
        return product - total_sum;

    }
};