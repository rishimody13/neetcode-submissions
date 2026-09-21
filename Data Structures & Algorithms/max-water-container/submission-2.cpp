#include <algorithm>
class Solution {
public:
    int maxArea(vector<int>& heights) {
        vector<int> a;
        int l = 0;
        int r = heights.size()-1;
        while (l<=r){
            a.push_back(min(heights[l], heights[r])*(r-l));
            if (heights[l]<=heights[r]){
                l++;
            }
            else{
                r--;
            }
        }
        return *max_element(a.begin(), a.end());
    }
};
