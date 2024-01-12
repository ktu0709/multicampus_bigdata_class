function checkFruit() {   
    // html에 있는 id = f_input를 찾아서 값을 리턴받자.  
    var fruit =  document.getElementById("f_select").value;
    var message; //p의 textContent에다 표시할 변수 

    switch(fruit){
        case "apple": message="Selected fruit is apple.";
                      break;
        case "banana": message="Selected fruit is banana.";
                      break;
        case "orange": message="Selected fruit is orange.";
                      break;
        default: message="Selected fruit is not apple.,,,,";
                      break;                            

    }//end switch 
  //  document.getElementById("result").textContent=message;
myp = document.getElementById("result");
console.log(typeof myp);
myp.textContent =  message;
myp.style.fontSize = "1.5em"; 

}//end function 
