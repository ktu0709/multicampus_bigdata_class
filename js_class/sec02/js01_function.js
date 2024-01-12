 //ex) 세과목의 총점, 평균을 연산하는 함수를 만들자.  
 //   조건  
 //  1. 각 과목의 점수를 리턴하는 함수를 만든다. 
 //  2. 총점, 평균을 연산하는 함수를 만든다.  
 //  3. 결과를 콘솔로 출력한다.  
 
 //1)  함수 선언   
 ///   1. 각 과목의 점수를 리턴하는 함수를 만든다. _국,영 ,수,
function getKor(){
    return 80;
}

function getEng(){
    return 90;
}

function getMat(){
    return 100; 
}
 //  2. 총점, 평균을 연산하는 함수를 만든다.  
function calcAvg(kor,eng,mat){
    const tot = kor+ eng+mat;
    const avg = tot/3 ;
    return avg;
}
 //  3. 결과를 콘솔로 출력한다.  
const res  = calcAvg(getKor(), getEng(), getMat());
console.log("avg = "+ res);





