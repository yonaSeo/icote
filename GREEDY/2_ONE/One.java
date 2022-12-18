import java.util.*;

public class One {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        int k = sc.nextInt();
        int result = 0;

        sc.close();

        while(true) {
            // N이 K로 나뉘어질 수 없을 때까지 1을 뺀다.
            int target = (n / k) * k;
            result += n - target;
            n = target;
            // N이 K보다 작아져 나눌 수 없으면 탈출한다.
            if (n < k) break;
            // K로 나눈다.
            n /= k;
            result++;            
        }
        result += (n - 1);
        System.out.println(result);
    }
}
