import java.util.*;

public class App {
    public static void main(String[] args) throws Exception {
        Queue<String> que = new LinkedList<>();

        que.offer("화사");
        que.offer("솔라");
        que.offer("문별");

        System.out.println(que);

        //que.poll();
        que.remove();

        System.out.println(que);

    }
}
