
//Sort an array of strings in alphabetical order

const footballClubs = ['Fcbarcelona','Real Madrid','Chelsea','Manchester United','PSG','Juventus'];
footballClubs.sort();
console.log(footballClubs);

console.log('=== or ===');

footballClubs.sort(function(a, b){return a-b});
console.log(footballClubs);

