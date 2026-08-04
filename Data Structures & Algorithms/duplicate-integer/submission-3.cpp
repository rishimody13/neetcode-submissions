class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        // unordered set 
        unordered_set<int> vals ;
        for (int i = 0; i<nums.size(); i++) {
            if (vals.count(nums[i])){ // count returns 1 if element exists otherwise 0
                return true;
            }
            vals.insert(nums[i]);
        }
        return false;
    }
};