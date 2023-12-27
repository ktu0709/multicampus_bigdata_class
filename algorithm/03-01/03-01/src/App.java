import java.util.*;

public class App {
    public static void main(String[] args) throws Exception {
        //배열
        String[] katok = {"다현","정연","쯔위","사나","지효"};

        for(int i=0;i<katok.length;i++){
            System.out.println(katok[i]);
        }

        System.out.println("==============");

        //리스트
        List<String> katok2 = new ArrayList<String>();
        katok2.add("다현");  //추가
        katok2.add("정연");
        katok2.add("쯔위");
        katok2.add("사나");
        katok2.add("지효");        
        System.out.println(katok2);
        //System.out.println(Katok2.get(3));
        katok2.remove(3);
        System.out.println(katok2);
        katok2.add(3, "모모");
        System.out.println(katok2);


    }
}

