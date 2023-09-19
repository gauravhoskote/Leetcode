class Solution {
    
    bool f(string s, set<string> ss, int p, int l, map<pair<int,int>, bool>& m){
        if(p+l>s.length())return false;
        if(m.find({p,l}) != m.end()){
            return m[{p,l}];
        }
        if(ss.find(s.substr(p,l)) != ss.end() && p+l == s.length())return true;
        bool b1 = ss.find(s.substr(p,l)) != ss.end() && f(s,ss,p+l,1,m);
        bool b2 = f(s,ss,p,l+1,m);
        m[{p,l}] = b1 || b2;
        return b1||b2;
    }
    
    
public:
    bool wordBreak(string s, vector<string>& wordDict) {
        set<string> ss;
        for(int i = 0; i < wordDict.size(); i++){
            ss.insert(wordDict[i]);
        }
        int p = 0,l = 1;
        map<pair<int,int>, bool> m;
        return f(s,ss,p,l,m);
    }
};
