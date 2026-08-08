class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        for (int i= 0; i<strs[0].size(); i++) { //tracks length of first word
            for (const string& s:strs){ //& means reference to - s is an aliance for the string element
                if (i == s.size() || s[i]!=strs[0][i]){
                    return s.substr(0, i); 
                }
            }
        }
        return strs[0];
    }
};