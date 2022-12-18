import java.util.Scanner;

public class Clock {
    public static int n = 0;
    public static int result = 0;

    public static boolean check(int h, int m, int s) {
        if (h % 10 == 3 || m % 10 == 3 || m / 10 == 3 || s % 10 == 3 || s / 10 == 3) {
            return true;
        }
        return false;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();
        sc.close();

        for (int i = 0; i < n + 1; i++) {
            for (int j = 0; j < 60; j++) {
                for (int k = 0; k < 60; k++) {
                    if (check(i, j, k))
                        result++;
                }
            }
        }

        System.out.println(result);
    }
}