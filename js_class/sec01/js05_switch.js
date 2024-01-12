//fruit변수에 과일을 대입해서 문구를 출력해보자. 
var fruit ="banana";


switch(fruit){
    case "banana": { console.log("Selected fruit is banana") ;
                    console.log("과일선택했어 ") ;
                    }
                    break;

    case "apple": console.log("사과 선택했어") ;
    case "과일" :   console.log("과일선택했어 ") ;  break;

    case "orange":  console.log("오렌지 선택했어") ;
    case "과일" :   console.log("과일선택했어 ") ;  break;
    default: console.log("Selected fruit is not apple,banana, or orange");
}

/*
switch(fruit){ 
    case "banana":  console.log("Selected fruit is banana") ; 
    case "과일" :   console.log("과일선택했어 ") ;  break;

    case "apple": console.log("사과 선택했어") ;   
    case "과일" :   console.log("과일선택했어 ") ;  break;
    
    case "orange":  console.log("오렌지 선택했어") ;  
    case "과일" :   console.log("과일선택했어 ") ;  break;
    default: console.log("Selected fruit is not apple,banana, or orange");  
}
*/
