
/*
  https://leetcode.com/problems/partition-equal-subset-sum/description/
*/

class Solution {
public:
    bool canPartition(vector<int>& nums) {
       bitset<10000>bits(1);
        int sum=0;
        for(int n:nums){
            sum+=n;
            bits|=bits<<n;
        }
        return (sum%2==0)&&(bits[sum/2]);
    }
};
