public class GrassHopper {

    public static int findAverage(int[] nums) {
        int avg = 0;
        int len = 0;
        for (int i = 0; i < nums.length; i++) {
            avg += nums[i];
            len += 1;
        }
        return avg / len;
    }
}
