import java.util.HashSet;
import java.util.Set;

class Solution {
    public int findClosestNumber(int[] nums) {
        int closest = nums[0];

        for (int x : nums){
            if (Math.abs(x) < Math.abs(closest)){
                closest = x;
            }
        }
    }
}