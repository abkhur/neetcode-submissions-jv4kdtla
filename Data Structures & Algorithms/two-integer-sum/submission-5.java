class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> seen = new HashMap<>();

        for (int i = 0; i < nums.length; i++) {
            int needs = target - nums[i];
            if (seen.containsKey(needs)) {
                return new int[]{seen.get(needs), i};
            }
            seen.put(nums[i], i);
        }
        return new int[]{-1,-1};
    }
}
