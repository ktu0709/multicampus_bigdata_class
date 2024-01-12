// ES6 = 2015  : 템플릿 문자열, let, 람다식, 클래스, [상속, 다형성]
//class  = 속성  + 메소드 (기능) , 각속성의 접근제한자, 상속() 재정의 , 다형성   ->클래스, 상속, 다형성    
//        각 이름 + 총점, 평균, 출력 
//  class  => 안에 선언된 변수(속성), 메소드  멤버라고 부른다.  
//                                 (생성자)
class Sung {   // class userName{}
  constructor(my_name="noname", kor=50, eng=50, mat=50) {   // constructor(){} -> 생성자 new연산자로 호출가능  
    this.my_name = my_name;
    this.kor = kor;
    this.eng = eng;
    this.mat = mat;
  }
//  constructor() {   // constructor(){} -> 생성자 new연산자로 호출가능    => 멤버변수 초기화  
//     this.my_name ="noname";
//     this.kor = 100;
//     this.eng = 100;
//     this.mat = 100;
//   }
  //총점을 계산하는 메소드 
  calculateTotal() {
    return this.kor + this.eng + this.mat;
  }
  //평균을 계산하는 메소드  
  calculateAverage() {
    return this.calculateTotal() / 3;
  }
  //멤버를 호출해서 출력하는 메소드  
  printScore() {
    const total = this.calculateTotal();
    const average = this.calculateAverage();
    console.log(`${this.my_name}'s Total: ${total}, Average: ${average}`);
  }
}
//new Sung("홍길동", 90, 80, 70); -> 초기값 전달 하면서 동적할당 -> 생성자호출  
//new 연산자는 동적할당 후 초기값 전달을 생성자를 통해서  실행된다.  
//new  = 동적할당  = 생성자  (멤버변수 초기화 )      
const s1 = new Sung("홍길동", 90, 80, 70);   // Sung클래스가 가진 constructor()를 자동호출 후 값대입 -> 메모리할당 
s1.printScore(); //기능형 메소드 
const s2 = new Sung();   // Sung클래스가 가진 constructor()를 자동호출 후 값대입 -> 메모리할당 
s2.printScore(); //기능형 메소드 

const s3 = new Sung("이길동");   // Sung클래스가 가진 constructor()를 자동호출 후 값대입 -> 메모리할당 
s3.printScore(); //기능형 메소드 

const s4 = new Sung("최길동",100);   // Sung클래스가 가진 constructor()를 자동호출 후 값대입 -> 메모리할당 
s4.printScore(); //기능형 메소드 

const s5 = new Sung("지길동",90,0,100);   // Sung클래스가 가진 constructor()를 자동호출 후 값대입 -> 메모리할당 
s5.printScore(); //기능형 메소드 



console.log(new Date().toString());
console.log(new Sung());

