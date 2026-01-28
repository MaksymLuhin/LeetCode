public class isPowerOfThree {
    public static boolean isPowerOfThree(int n) {
        if(n == 1) {
            return true;
        }
        else if(n < 0 || n % 3 != 0) {
            return false;
        }
        else if(n >= (Math.pow(2,31)-1) || n <= -Math.pow(2,31) ) {
            return false;
        }
        
        return isPowerOfThree(n/3);
    }

    public static void main(String[] args) {
        System.out.print(isPowerOfThree(27));
    }
}
