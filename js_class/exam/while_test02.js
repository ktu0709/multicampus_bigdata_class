//테이블을 동적으로 생성하고 싶다.  
//<table><tr><td></td></tr></table>  :  <th><thead><tbody><tfoot>   
// <table><thead><th><tr><td> </td></tr></th></thead></table>
var tableData  = [
      {my_name :"홍길동01" , addr :"서울01" , tel :"0201-000-0000"} , 
      {my_name :"홍길동02" , addr :"서울02" , tel :"0202-000-0000"} , 
      {my_name :"홍길동03" , addr :"서울03" , tel :"0203-000-0000"}   

];
/////////table, thead, tbody 
var table = document.createElement("table"); 
var thead = document.createElement("thead"); 
var tbody = document.createElement("tbody"); 

 ///table header 
 var headerRow = document.createElement("tr"); 
 var header  = Object.keys(tableData[0]); 

///th  
for (var i= 0 ;  i < header.length ;i++ ) {  //for(초기값 ; 비교 ;  증가){} 
  var th =document.createElement("th");  
  th.textContent = header[i]; 
  headerRow.appendChild(th); 
}
thead.appendChild(headerRow) ;
table.appendChild(thead);

/////////create table rows   -> while 

var rowIndex =0;
while(rowIndex  < tableData.length) {  //줄 반복적으로 ....  
     //줄
  var row  =  document.createElement("tr");
     //칸  = 데이터가 가진 값의 인덱스 만큼 
      for(var j = 0 ; j <header.length ; j++){  // 칸을 반복적으로..
            var td  =  document.createElement("td");
            td.textContent = tableData[rowIndex][header[j]];
            row.appendChild(td);
      }
      tbody.appendChild(row);
      rowIndex ++; 
    }

table.appendChild(tbody);
var my_res  = document.getElementById("container");
my_res.appendChild(table);
/////////////테이블 보더 1 , 솔리드, 파랑, 배경색 핑크 
///////////////테이블 td의 폰트 사이즈  1.5em
