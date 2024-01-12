/* 자바스크립트 데이터 타입 : typeof  */ 
// [const, let], var 
//Number
const age =25;   // age 변수에 25를 대입했다. -> 상수화 
console.log(typeof age  + "\t\t\t" + age); // age 타입을 확인  
 
 //String, ' '  " "
 const m_name ='홍길동';
 const addr="서울";
 console.log(typeof m_name + "\t\t\t" + m_name);
 console.log(typeof addr+ "\t\t\t" + addr);
 

 //Boolean, 
 const isStudent =true ;
 console.log(typeof isStudent+"\t\t\t" + isStudent);//boolean 

 //Undefined, 
 let myvar;
console.log(typeof  myvar + "\t\t\t" + myvar);
 
 //Null, 
 const  m = null;  // object를 초기화 하는 키워드 
 console.log(typeof  m+ "\t\t\t" + m);
 
// Object,
const person={ 
        m_name : '홍길동',
        addr   : "서울"
};
 console.log(typeof  person+ "\t\t\t" + person.m_name +"\t "+ person.addr);


 //Array, : 하나의 변수에 나열형 인덱스로 값을 저장하는  것  
const numbers =[1,2,3,4,5]; 
console.log(typeof numbers+ "\t\t\t" + numbers ); //object 
console.log(typeof numbers+ "\t\t\t" + numbers[0] ); //object 
console.log(typeof numbers+ "\t\t\t" + numbers[1] ); //object 
console.log(typeof numbers+ "\t\t\t" + numbers[2] ); //object 
console.log(typeof numbers+ "\t\t\t" + numbers[3] ); //object 
console.log(typeof numbers+ "\t\t\t" + numbers[4] ); //object 
console.log(numbers[4] + numbers[0]);

 //Function ,
const  add = function(a,b){
    return a+b;
};
console.log(typeof add+"\t\t\t" + add(10,20) +"\t" + add(numbers[4],numbers[0] )); //function 
 
 //Symbol 
 const id =Symbol('uniqueId');
 //console.log(typeof id +"\t\t\t"+ id);  //symbol



