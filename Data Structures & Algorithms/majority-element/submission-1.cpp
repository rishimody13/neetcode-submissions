class Solution {
public:
    int majorityElement(vector<int>& nums) {
        int ans = nums[0];
        int count = 1;
        for (const int& i:nums ){
            if (count==0){
                ans = i;
            }
            if (i != ans){
                count--;
            }
            if (i==ans){
                count++;
            }
        }
        return ans;
    }
};