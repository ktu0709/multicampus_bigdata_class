let numbers = [ 1, 2, 3, "4", 5]; // Object Array -> 요소를 인덱스로 관리  = CRUD 
let length = numbers.length;
for (let i = 0; i < length; i++) {
  console.dir(numbers[i]);
}
console.dir(typeof numbers);

let fruitsArr = ['사과', '딸기', '바나나', '수박', '복숭아'];

//1 .딸기를  인덱스를 찾아 출력 해보자.  
console.dir(fruitsArr.indexOf('딸기'));

//2. 맨뒤에 자몽을 추가해보자  
console.dir(fruitsArr.push('자몽'));
console.dir(fruitsArr)

//3. 맨뒤에 요소를 삭제 해보자.    
console.dir(fruitsArr.pop());  // 맨뒤에 삭제되는 요소를 리턴 
console.dir(fruitsArr)

//4. 맨앞에 포도를 추가하자. 
console.dir(fruitsArr.unshift('포도')); 
console.dir(fruitsArr)

//5. 맨앞에 요소를 제거해 보자.  
console.dir(fruitsArr.shift()); 
console.dir(fruitsArr);

//6. 데이터를 배열로 만들어 결합해보자  concat(결합할 오브젝트) 
let myFruit =['참외' ,'방울토마토','체리','메론'] ;
let arHap =fruitsArr.concat(myFruit); 
console.log(arHap + ": " + "\t" +  arHap.length);
console.dir(fruitsArr);

//7.정렬해보자.  
let ch ='참외';    // ''," ".''' ''' ->String ->[char,,,,,,] -> 인덱스로 찾아올수 있다. 
//  ['참','외]  [0] [1]
console.log("참의 코드값  :" + ch.charCodeAt(0)) ;//52280
console.dir(fruitsArr.sort() ); //클로저


function compareNumbers(a, b) {
   return a - b;
 }

let  my_numbers = [4, 2, 5, 1, 3];
// my_numbers.sort(function(a, b) { //함수식 = 핸들링 
//  console.log(a +" : " +b  );
//   return a - b;
// });
my_numbers.sort(compareNumbers);   
// 클로저  : 외부(둘러싸고 있는) 에서 실행이 완료되면 둘러싸고 있는 범위에서 엑세스 할수 있는기능
//    -> 내부함수가 외부함수내에서 정의가 되고  내부함수가 외부함수 범위의 변수를 참조할 때 생성되는 것을 말한다. 
//    -> [내부함수는 참조하는 변수와 함께 클로저를 형성했다 ]

//Tip:  클로저에 의해 참조되는 변수는 클로저 자체에 더 이상 도달할수 없을때 까지 가비지 수집되지 않으므로
// 클로저와 메모리 사용에 영향을 미치는 잠재적인 부분을 고려해야 한다.  
console.log(my_numbers);

//8.  fruitsArr의 요소들을 글자 수 기준으로 오름차순으로 정렬해보자 . 
//   만약에 글자수가 같다면 , 가나다순으로 내림차순 정렬을 해보자.  

function my_compare(a,b){
      //if(a.length  !=  b.length) return a.length - b.length;       
    if (a.length === b.length) {  
         return b < a ? -1 : 1; //길이가 같으면 내림차순
      }
    return a.length - b.length;
}

fruitsArr.sort(my_compare);   
console.dir(fruitsArr);


//9. 매개인자를 통해서 추가, 수정,삭제 ,복사를 한번에 하는  splice()를 사용해보자.  
 //array.splice(start[, deleteCount[, item1[, item2[, ...]]]])  
console.dir("9-1 ) 2번 인덱스를 삭제해 보자. ");  
console.dir(fruitsArr.splice(2,1 ) ) ;
console.dir(fruitsArr);

console.dir("9-2. 1번인덱스 과일 2개을 추가해 보자. ");
console.dir(fruitsArr.splice( 1,0,"토마토","메론") ) ;
console.dir(fruitsArr);

console.dir("9-3. 3번인덱스에 수정");
console.dir(fruitsArr.splice(3,1,'라즈베리' ) ) ;
console.dir(fruitsArr);

console.dir("10 . 원하는 위치의 배열을 복사해 보자.  ");
console.dir(fruitsArr.slice(2,4 ) ) ;
console.dir(fruitsArr);












