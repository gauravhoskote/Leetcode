class Solution {
public:

    int fib(int n) {
        if(n <= 1)return n;
        int x,y;
        x = 0;
        y = 1;
        int z;
        for(int i = 2; i <= n; i++){
            z = x+y;
            x = y;
            y = z;
        }
        return z;
    }
};
