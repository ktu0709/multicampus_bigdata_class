import java.util.*;

public class App {

    public static class CircularQueueList{
        private LinkedList<String> list;
        private int capacity;

        public CircularQueueList(int capacity){
            this.list = new LinkedList<>();
            this.capacity=capacity;
        }

        public boolean isEmpty(){
            return list.isEmpty();
        }

        private boolean isFull(){
            return list.size() == capacity;
        }

        public void Enqueue(String item){
            if(isFull()){
                System.out.println("Queue is Full");
                return;
            }
            list.add(item);            
        }

        public String Dequeue(){
            if(isEmpty()){
                System.out.println("Queue is Empty");
                return null;
            }
            String removeItem = list.removeFirst();
            return removeItem;         
        }

        public String peek(){
            if(isEmpty()){
                System.out.println("Queue is Empty");
                return null;
            }
            return list.getFirst();
        }
    }

    public static void main(String[] args) throws Exception {
        CircularQueueList que = new CircularQueueList(5);

        que.Enqueue("화사");
        que.Enqueue("솔라");
        que.Enqueue("문별");

        System.out.println("Front: " + que.peek());
        
        que.Dequeue();
        System.out.println("Front: " + que.peek());

    }
}
