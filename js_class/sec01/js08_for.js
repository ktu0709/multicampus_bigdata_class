// 1~ 10까지 for출력 해보자.  
for(var i =1 ; i <= 10   ;   i++){
    console.log(i);
}

// 10~ 1까지 for출력 해보자.   
for(var i =10 ; i >= 1   ;   i--){
    console.log(i);
}

// 숫자에 2을 나눈 나머지가  0이면 짝수, 그렇지 않으면 홀수  

//1~ 100 까지  홀수만 출력   
for(var i =1 ; i <= 100   ;   i++){
     if( i % 2 != 0     ) {
    console.log(i);
     }
}
//  1~ 100까지 짝수만 출력  
for(var i =1 ; i <= 100   ;   i++){
      if(  i % 2 === 0    ) {
            console.log(i);
      }
}

 //   1~ 100까지 출력을 하되 2의 배수이면서  3의 배수를 출력 해보자.  

for(var i =1 ; i <= 100   ;   i++){
      if(  i % 2 === 0  && i % 3===0   ) {
            console.log(i);
      }
}

var tableData  = [
      {my_name :"홍길동01" , addr :"서울01" , tel :"0201-000-0000" , cell:"010-0000-0000"} ,
      {my_name :"홍길동02" , addr :"서울02" , tel :"0202-000-0000"} , 
      {my_name :"홍길동03" , addr :"서울03" , tel :"0203-000-0000"}   

];

for(var  i=0 ; i <= tableData.length-1 ; i++){   
      console.log(tableData[i] );
}

console.log(Object.keys(tableData[0])); 
console.log(Object.keys(tableData[1])); 
console.log(Object.keys(tableData[2])); 
console.log(Object.values(tableData));
console.log(Object.values(Object.keys(tableData[0])));


// Parenthesize the whole initializer
// 전체 초기화 부분을 ()로 묶어서 사용 for + in + ? :
// "start" in window : "start"가 window 객체에 속성이 있는지 확인
// window.start : 0 -> "start"속성이 존재하면 window.start를 리턴
for (let i = ("start" in window ? window.start : 0); i < 9; i++) {
  console.log(i);
}

// Parenthesize the `in` expression
for (let i = ("start" in window) ? window.start : 0; i < 9; i++) {
  console.log(i);
}

for (let i = 0; i < 3; i++) {
  setTimeout(() => {
    console.log(i);
  }, 1000);
}




