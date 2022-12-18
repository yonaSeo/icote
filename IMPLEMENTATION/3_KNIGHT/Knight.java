import java.util.Scanner;

public class Knight {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String inputData = sc.nextLine();
        sc.close();
        
        int row = inputData.charAt(1) - '0';
        int col = inputData.charAt(0) - 'a' + 1;

        int cnt = 0;

        int[] dx = { -2, -2, -1, -1, 1, 1, 2, 2 };
        int[] dy = { -1, 1, -2, 2, -2, 2, -1, 1 };

        for (int i = 0; i < 8; i++) {
            int nextRow = row + dx[i];
            int nextCol = col + dy[i];

            if (nextRow >= 1 && nextCol >= 1 && nextRow <= 8 && nextCol <= 8) {
                cnt++;
            }
        }
        System.out.println(cnt);
    }
}