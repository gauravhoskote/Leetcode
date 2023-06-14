class Solution {
public:
    int partitionString(string s) {
        set<char> ss;
        int ctr = 0;
        for(int i = 0; i < s.length(); i++){
            if(ss.find(s[i]) == ss.end()){
                ss.insert(s[i]);
            }else{
                ss.clear();
                ss.insert(s[i]);
                ctr++;
            }
        }
        ctr++;
        return ctr;
        
    }
};
