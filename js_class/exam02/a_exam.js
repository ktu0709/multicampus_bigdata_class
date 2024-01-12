function add(num){
    return num+2;
}

function sub(num){
    return num-2;
}

function mul(num){
    return num*2;
}

function div(num){
    return num/2;
}

function Result(op){
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

}