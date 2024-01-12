//만일에 나이가 19 보다 크면  P태그안에 "어른이야"출력하자, 
//그렇지 않으면 "청소년이야"를 출력하자. 
var age =18;
 
if(age >= 19 ){    
//html 태그의 엘리먼트를 id로 찾아서 textContent에다가 출력하자. 
  document.getElementById("message").textContent= "I'm an adult";
}else{
//document.getElementsByTagName("p").textContent="청소년이야";
document.getElementById("message").textContent="청소년이야";
}

