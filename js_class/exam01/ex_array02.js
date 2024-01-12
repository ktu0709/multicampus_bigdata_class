// ES6 문법을 활용한 메소드 호출
/*
화살표함수 , 클래스 , 모듈,템플릿 문자열 ${}, 리소스 해제등 추가한 문법
*/
//Array join, filter, find, map, flatMap 

let fruitsArr = ['사과', '딸기', '바나나', '수박', '복숭아'];
console.dir("1) join test  ");
console.dir(`[ ${fruitsArr.join('][')} ]`) ;

// arr.filter(callback(element[, index[, array]])[, thisArg])
console.dir("2) filter test : 조건 추출  "); 
console.dir(fruitsArr.filter(function(e){  
      return e.length ==2;
} ));

console.dir(fruitsArr.filter(e => e.length ==2));
console.dir(fruitsArr.filter(r => r.length ==3));

console.dir("3) find test : 요소를 찾는다.  "); 
console.dir(fruitsArr.find(function(e){
    //console.log(e.search('메론')  );
    return  e.search('사')  > -1;

}));

console.dir(fruitsArr.find(e =>  e.search('박')  > -1) );



console.dir("4) map test : 요소 연산  "); 
//각 요소의 첫글자만 추출해서 배열로 리턴받자.  
console.dir(fruitsArr.map( e  => e[0] )); 

console.dir("5) flatMap test : 요소 연산  "); 
//각 요소의 첫글자만 추출해서 배열로 리턴받자.  
console.dir(fruitsArr.flatMap( e  => e[0] )); 


let arr1 = ["it's Sunny in", "", "California"];
console.dir(arr1.map(x=>x.split(" "))) ;
console.dir(arr1.flatMap(x => x.split(" ")));

console.dir( [1,2,3,4,5].map(e => [e, e*2]));  // 배열의 배열 
console.dir( [1,2,3,4,5].flatMap(e => [e, e*2]));    // 단일배열  = 1차원 배열 