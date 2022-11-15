
//Create a length converter function
function lengthConverter(numInm,to){
    let result=0;
        var unit = {
            'cm': 100,
            'km': 0.001,
            'mm': 1000,
        }
        for(var key in unit){
            result = numInm * unit[to];
        }
        return result;
    }
    console.log(lengthConverter(27, 'cm'));