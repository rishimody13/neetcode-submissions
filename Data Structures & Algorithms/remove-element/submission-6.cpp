class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        int j = 0;
        for (int i =0; i<nums.size(); i++){
            if (nums[i]!=val){
                nums[j++]=nums[i];
                //nums[j++] means access nums[j] then increment j by 1
            }
        }
        return j;
    }
};