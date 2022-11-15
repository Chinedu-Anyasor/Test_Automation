//we cant use const because the starting value will increase over time, we use let

let star = 10 //start point
while (star >=1){
    if (star ===1) {
        console.log(star + ' star')
    } else {
        console.log(star + ' stars')
    }
    star = star - 1
}