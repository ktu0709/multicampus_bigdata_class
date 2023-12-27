public class App {

    //Node Class
    public static class Node<E>{
     E data;
     Node<E> next;
     
     public Node(E data){
        this.data = data;
        this.next = null;
     }
    }

    //list class
    public static class CircularLinkedList<E>{
        private Node<E> head;

        public CircularLinkedList(){
            this.head = null;
        }

    //추가
    public void add(E data){
        Node<E> newNode = new Node<>(data);

        if(head == null){
            head= newNode;
            head.next = head;            
        }
        else{
            Node<E> temp = head;
            while(temp.next != head){
                temp = temp.next;
            }
            temp.next = newNode;
            newNode.next = head;
        }
        }
        //삭제
        public void remove(E data){
            if(head == null){
                System.out.println("No Node");            
            }
            Node<E> current = head;
            Node<E> prev = null;

            while(current.data != data){
                if(current.next == head){
                    System.out.println("can`t find Node");     
                }
                prev = current;
                current = current.next;
            }
            
            //삭제할 노드가 헤드인 경우
            if(current == head){
                if(current.next == head){
                    head = null;
                }
                //리스트에 노드가 여러개 있을 경우
                else{
                    prev = head;
                    while(prev.next != head){
                        prev=prev.next;
                    }
                    head=current.next;
                    prev.next = head;
                }
            }
            else{
                prev.next=current.next;
              }
        }

        public void display(){
            if(head == null){
                System.out.println("No Node");
            }

            Node<E> current = head;
            do{
                System.out.print(current.data + " ,");
                current  = current.next;                
            }while(current != head);
            System.out.println();
        }
    }


    public static void main(String[] args) throws Exception {
        CircularLinkedList<String> katok = new CircularLinkedList<>();

        katok.add("다현");
        katok.add("정연");
        katok.add("쯔위");
        katok.add("사나");
        katok.add("지효");

        katok.remove("쯔위");

        katok.display();

    }
}
