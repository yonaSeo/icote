import java.util.ArrayList;
import java.util.Collections;
import java.util.Scanner;

public class Guild {

    public static int n;
    public static ArrayList<Integer> arrayList = new ArrayList<>();
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();

        for (int i=0; i<n; i++) {
            arrayList.add(sc.nextInt());
        }

        Collections.sort(arrayList);
        sc.close();

        int result = 0;
        int cnt = 0;
        
        for (int i=0; i<n; i++) {
            cnt++;
            if (cnt >= arrayList.get(i)) {
                result++;
                cnt = 0;
            }
        }

        System.out.println(result);
    }    
}
