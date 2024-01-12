const add = num=>num+2;
const sub = num=>num-2;
const mul = num=>num*2;
const div = num=>num/2;

const Result=op =>{
    var num = parseFloat(document.getElementById("numberInput").value)
    var res = 0;
    switch(op){
    case 'add':
                res = add(num); break;
    case 'sub':
                res = sub(num); break;
    case 'mul':
                res = mul(num); break;
    case 'div':
                res = div(num); break;

    }
    alert('Result : ' + res);
    /*
    document.getElementById("calc_res").textContent = "결과는" + res;
    document.getElementById("calc_res").innerText = "결과는" + res;
    console.log(document.getElementById("calc_res").nodeName);
    console.log(document.getElementById("calc_res").nodeType);
    */
    p_tag = document.getElementById("calc_res");
    p_tag.style.color = 'red';
    p_tag.innerText = "결과" + res;

}