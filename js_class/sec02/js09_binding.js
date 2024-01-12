//js 묵시적(자동) , 명시적인 바인딩  

// 1) 묵시적(자동)  바인딩  = implicit Binding 
//  : 함수가 객체의 메소드로 호출되면 'this' 키워드는 메소드가 호출된 
//  객체에 자동으로 바인딩이 된다.  

const obj ={ myname:"홍길동",   myname02:"홍길동02", 
             sayHollo :  function() {
               console.log(`Hello, ${this.myname}!,${this.myname02}! `);
               } };

obj.sayHollo(); 
console.log(typeof obj);

//2) 명시적인 바인딩    call(), apply(), bind() ---> this 허용하겠다.  
 function sayHollo02() {
                     console.log(`Hello, ${this.myname}! `);
                }

sayHollo02();

const obj01  ={myname : "정길동"} ;
const obj02  ={myname : "박길동"} ;

sayHollo02.call(obj01);
sayHollo02.apply(obj02);

const  bindres  = sayHollo02.bind(obj01);
bindres();

//3) 번외편  
const obj04 ={ myname:"홍길동111",   myname02:"홍길동2222", 
             sayHollo :  function() {
                const greet =() =>{
                                    console.log(`Hello, ${this.myname}!,${this.myname02}! `);
                                  };   
                greet();
            } };

obj04.sayHollo(); 
console.log(typeof obj04);

console.log("\n\n\n================[4) 프로토 타입 번외편] ===================================");
//4) 프로토 타입 번외편 
function Animal() { }  // 특정한 구성은 없지만 인스턴스를 생성할 수 있다. 

Animal.prototype.speak = function() {  // Animal의 생성자에게 매개로 전달 된다.  
  return this;
}

Animal.eat = function() {  // Animal의  함수로 추가  
  return this;
}
let obj05 = new Animal(); // 객체 생성 
let speak = obj05.speak; 
speak(); // global object (in non–strict mode)

let eat = Animal.eat;
eat(); // global object (in non-strict mode)

console.log("\n\n\n================[5)  4번을 클래스로 만들자  ===================================");
class Animal02{
    
   speak() {  // Animal의 생성자에게 매개로 전달 된다.  
     return this;
  }
  static eat(){
     return this;
  }
}
let obj06 = new Animal02(); // 객체 생성 
let speak02 = obj06.speak; 
console.log(speak()); // global object = window  브라우저 객체 (in non–strict mode)

let eat02 = Animal02.eat;
console.log(eat()); // global object= window 브라우저 객체 (in non-strict mode)

////////// 4,5번은 명시적 바인딩이 없이 함수를 호출하거나 특정 메소드를 호출해서 리턴하는 경우  









