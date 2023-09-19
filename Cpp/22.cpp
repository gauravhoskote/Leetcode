class Solution {
public:
    void f(int opened, vector<string> &arr, string s, int n){
        int closed = s.length() - opened;
        if(n == opened){
            if(opened == closed){
                arr.push_back(s);
                return;
            }else{
                if(closed < opened){
                    f(opened, arr, s+')', n);
                    return;
                }
            }
        }
        else{
            if(opened > closed){
                f(opened, arr, s+')', n);
                f(opened+1, arr, s+'(', n);
                return;
            }else{
                f(opened+1, arr, s+'(', n);
            }
        }
        return;   
    }

    vector<string> generateParenthesis(int n) {
        vector<string> arr;
        f(0, arr, "",n);
        return arr;
    }
};
