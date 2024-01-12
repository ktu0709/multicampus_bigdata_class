//1. div id를 찾아온다. document.getElementById("container")
//2  p 태그를 생성하고 싶다.  document.createElement("p");
//3 div, p :  appendChild() 
//문제 : while 반복문을 이용해서 반복의 횟수만큼 태그를 생성해보자.  

var count =1;
var my_container = document.getElementById("container"); //  my_container = div

while(count  <= 5){
  var my_p  = document.createElement("p");
  my_p.textContent = "count : "+ count;
  my_container.appendChild(my_p );
    count++ ; 
}
