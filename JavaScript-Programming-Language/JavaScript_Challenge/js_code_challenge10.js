
//Create  a  function  that  filters  out  negative numbers
var array = [16, -30, 26, 8, -70]

 array = array.filter(function(x) {return x > -1;});

 console.log(array);


 console.log('=== or ===');

function negativeNumbers(arr){
    return arr.filter((num) => num > -1)
  }

  console.log(negativeNumbers([1,1,3,2,-6,-3,10,-3,-5]));
  