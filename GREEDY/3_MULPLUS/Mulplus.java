import java.util.*;

public class Mulplus {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String str = sc.next();
        sc.close();

        long result = str.charAt(0) - '0';
        
        for (int i=1; i<str.length(); i++) {
            int num = str.charAt(i) - '0';
            if (num <= 1 || result <= 1) {
                result += num;
            } else {
                result *= num;
            }      
        }

        System.out.println(result);
    }
}
