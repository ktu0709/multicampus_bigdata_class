import java.util.*;

public class App {
    public static void main(String[] args) throws Exception {
        Stack<String> stk = new Stack<>();
        
        stk.push("커피");
        stk.push("녹차");
        stk.push("꿀물");
        stk.push("콜라");
        stk.push("환타");

        System.out.println(stk);

        stk.pop();
        System.out.println(stk);
    }
}
