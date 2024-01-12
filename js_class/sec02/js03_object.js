//클래스  -> Object 객체 생성  -> 값을 출력
//클래스  = 속성 + 기능 
//클래스  = userDataType   = 사용자가 만드는 자료형  
//ex) 이름, 국어, 영어, 수학   -> 하나의 이름으로 등록해서 값만 전달할 수 있도록 설계하자. 
//  sung(my_name,kor,eng,mat)
//    홍길동  100 100 100  s1
//    정길동   90  90 90   s2
//    박길동   70  70  70  s3  -> 변수 =값  ;  -> 호출 -> 12 

////////1) sung(my_name,kor,eng,mat)로 객체를 선언   
// this  = 현재 오브젝트를 지칭하는 연산자.  
function sung(my_name,kor,eng,mat){
  this.my_name = my_name; //이름 
  this.kor  = kor ;  // 국어 
  this.eng = eng;     //영어
  this.mat = mat;    // 수학  
}

//////2) 객체를 생성  -> 레코드 생성     [new 연산자로 객체를 생성  -> 동적할당 ] 
s1  = new  sung("홍길동",100,100,100);   // s1이라는 객체가 생성되고 값전달이 된다.  
s2  = new  sung("정길동",90,90,90); 
s3=   new sung("박길동",70,  70,  70  );

console.log( s1.my_name + "\t" + s1.kor +"\t" + s1.eng +"\t" + s1.mat); 
console.log( s2.my_name + "\t" + s2.kor +"\t" + s2.eng +"\t" + s2.mat); 
console.log( s3.my_name + "\t" + s3.kor +"\t" + s3.eng +"\t" + s3.mat); 

s4=s1;
console.log( s4.my_name + "\t" + s4.kor +"\t" + s4.eng +"\t" + s4.mat); 

s4.my_name="1111111111";
console.log( s4.my_name + "\t" + s4.kor +"\t" + s4.eng +"\t" + s4.mat);
console.log( s1.my_name + "\t" + s1.kor +"\t" + s1.eng +"\t" + s1.mat);