
//Return a Boolean if a number is divisible by 10

let num = 40;
let result = num % 10 == 0 ? true : false;
console.log(result);

console.log('=== OR ===');

let i = 35;
if (i % 10 == 0) {
    console.log(true);
} else {
    console.log(false);
}

console.log('=== OR ===');

const number = function() {
    let num = newNum();
    let testResult = num % 10;
    if(testResult == 0){
        console.log(true);
    } else {
        console.log(false);
    }
}

newNum(20);