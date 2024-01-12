// Object 클래스의 재정의 메소드를 구현한 Person확인  
class Person{
  constructor(my_name , age ){
     this.my_name=my_name;
     this.age = age;
     console.log("-----------");
  }

   toString(){  // 재정의 한  메소드  
       return  "내꺼 ";
  }
}

console.log(new Person("홍길동", 10));
console.log(new Person("홍길동", 10).toString());
//객체를 p1으로 생성 한 후p1을 출력해보자. 

p1  =  new Person("1111", 11); // p1 = Object()-> Person() 

console.log(p1.toString());  // 내꺼 

