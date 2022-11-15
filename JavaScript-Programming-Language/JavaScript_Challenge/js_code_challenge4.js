
//Print a table containing multiplication tables

function multiplicationTable (){
    let table = []; 
    let result; 
    for (let i = 1; i <= 10; i++) {
        for (let j = 1; j <= 12; j++) {
            result = i *j;
            table.push(i + '' +'*' + '' + j + '=' + result);
        }
    }
    return table;
}
console.log(multiplicationTable());
