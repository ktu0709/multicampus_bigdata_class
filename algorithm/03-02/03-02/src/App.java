import java.util.*;

public class App {
     private static List<String> katok = new ArrayList<String>();

    public static void main(String[] args) throws Exception {
       
        add_data("다현");
        add_data("정연");
        add_data("쯔위");
        add_data("사나");
        add_data("지효");
        
        System.out.println(katok);


        insert_data(2,"모모");
        System.out.println(katok);

        delete_data(4);
        System.out.println(katok);

    }

    public static void add_data(String str){
        katok.add(str);
    }

    public static void insert_data(int pos , String str){
        katok.add(pos, str);
    }

    public static void delete_data(int pos){
        katok.remove(pos);
    }

}
