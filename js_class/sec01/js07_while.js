//배열과 반복문  : 하나의 변수에 나열형으로  []를 이용해서 값을 관리하는 것  = 배열 
// 배열은 값을 인덱스로 관리한다.  0
// 배열은 각각의  데이터를 요소라고 부르고 엘리먼트라고 칭한다.  
// 배열은 선언과 동시에 개수를 length로 속성을 제공한다.  
// 배열의 length, 인덱스는 1 차이가 난다. 
var myArray = [1,2,3,4,5]; 

// console.log(myArray) ;
// console.log(myArray[0] ) ; 
// console.log(myArray[1] ) ;
// console.log(myArray[2] ) ;
// console.log(myArray[3] ) ;
// console.log(myArray[4] ) ;
console.log("개수 :"+ myArray.length);
// 0~ 4번지 인덱스 까지    ++ 하면서 반복문으로 출력하고 싶다.  
//  myArray[0] ~ myArray[4]   ++ 하면서 반복문으로 출력하고 싶다
// myArray[i]  -> i  0~ 4 ++증가하면서 출력 했으면 좋겠다. 
///////////
var  i = 0 ; 
while(i  <=  myArray.length-1) {  
  console.log(myArray[i]);
   i++;
}
var tableData  = [
      {my_name :"홍길동01" , addr :"서울01" , tel :"0201-000-0000"} , 
      {my_name :"홍길동02" , addr :"서울02" , tel :"0202-000-0000"} , 
      {my_name :"홍길동03" , addr :"서울03" , tel :"0203-000-0000"}   

];
 i = 0 ; 
while(i  <=  tableData.length-1) {  
  console.log(tableData[i]);
   i++;
}
//"홍길동03" / 서울02  
console.log(tableData[2].my_name);
console.log(tableData[1].addr);

//////////// tableData의 있는 이름만 추출을 해보자.  
i = 0 ; 
while(i  <=  tableData.length-1) {  
  console.log(tableData[i].my_name);
   i++;
}
///////////////////tableData의 있는    이름:전화번호 로 출력해보자.  
i = 0 ; 
while(i  <=  tableData.length-1) {  
  console.log(tableData[i].my_name +" : " + tableData[i].tel);
   i++;
}
///반복변수  =for, while  = i,j,k,l,m,n  ->포트란 
// count , sum 누적데이터변수  , tot = 점수   







