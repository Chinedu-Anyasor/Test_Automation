

//Calculate the sum of numbers within an array

let scores = [10,14,20,15,25,34];
let sum = 0;
for(let i=0; i< scores.length; i++) {
    sum += scores[i]; // sum = sum + scores[i];
}
console.log(sum);


function sumArry(arr) {
    let total = 0;

    for(i = 0; i < arr.length; i++ ) {
        total += arr[i];
    }
    return total;
}

console.log(sumArry([1,2,3,4,5,6]));