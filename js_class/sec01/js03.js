//1)비교연산자.  
var a = 5;
var b = 10;
var c = "5";

console.log(a == b);      
console.log(a != b);     
console.log(a === c);    
console.log(a !== c);    
console.log(a > b);      
console.log(a < b);      
console.log(a >= b);     
console.log(a <= b);     

//2) 비트연산
var a = 2, b = 7, c;
c = a & b;
console.log(" 2 & 7 는 "+c);  // 2 && 7  = 7 ?     7 && 2  =   2 

c = a | b;
console.log("2 | 7 는 "+c); 
c = a ^ b;
console.log("2 ^ 7  는 "+c);

//3) 논리연산  
 a = 5; 
 b = 10;
 var result = a > 0  &&   b<20;  // true &&  true  = true
 console.log(result) 
 console.log( 0 &&  7 &&   0 &&  9 ) ;   // false
console.log( 0 || 0|| 0 || 10  || 7 || 0  ) ;    //true 
   

  // 논리합일 경우 왼쪽에 있는 피연산자의 결과가 true 이면 나머지연산안하고 true를 리턴
  // 논리곱일 경우 왼쪽에 있는 피연산자의 결과가 false  이면 나머지연산안하고 false를 리턴
                                                          
/*

		     0000000000000010  (2)
      |  0000000000000111  (7)
       _________________________
         0000000000000111  (7)

       
       
           0000000000000010  (2)
       &   0000000000000111  (7)
	   _________________________
           0000000000000010  (2)




         0000000000000010  (2)
     ^   0000000000000111  (7)
_______________________________
         0000000000000101  (5)

 */