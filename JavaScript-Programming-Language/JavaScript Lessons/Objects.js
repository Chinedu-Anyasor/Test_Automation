// const myObject = {name:'car', colour:'red', price:25000}

// const door = {
//     isOpen: false,
//     material: 'wood',
//     height: 8,
//     toggleOpenAndClose: function(){
//         if(door.isOpen===true){
//             door.isOpen = false
//         } else{
//             door.isOpen = true
//         }
//     }
// }

// door.toggleOpenAndClose() 'Richard', 'Ken', 'Jane'

// const person = {
//     name:'Nick',
//     age: 24,
//     siblings: [
//         {
//             name: 'Richard',
//             age: 20,
//         },
//         {
//             name: 'Ken',
//             age: 17,
//         },
//         {
//             name: 'Jane',
//             age: 27,
//         }
//     ],
//     addSibling: function(name){
//         person.siblings.push(name)
//     }
// }

// person.addSibling({
//     name: 'Henry',
//     age: 0
// })
// console.log(person.siblings[0])







// ///console.log(door.isOpen)

// const books = {[]
//     title: 'Rich Dad, Poor Dad',
//     description: 'Investment',
//     numberOfPages: '266',
//     author: 'Robert Kiyosaki',
//     reading: false,
//     toggleReadingStatus: function(){
//         if(books.reading===true){
//             books.reading = false
//         }else{
//             books.reading = true
//         }

//     }

// }
// books.toggleReadingStatus()
// console.log(books)

const books = [{
    title: 'Rich Dad, Poor Dad',
    description: 'Investment',
    numberOfPages: '266',
    author: 'Robert Kiyosaki',
    reading: false,
},
{
    title: 'Thinking for a change',
    description: 'Motivational',
    numberOfPages: 266,
    author: 'John Maxwell',
    reading: true,
},
{
    title: 'The power of influence',
    description: 'Leadership',
    numberOfPages: 157,
    author:'John Maxwell',
    reading: true,
},
]

for(let i=0; i < books.length; i++){
    if (books[i].reading ===true){
        console.log(books[i])
    }
}

// for(const title of books){
//     if(title.reading===true){
//         console.log(title)
//     }
// }



//    for(let start = 0; start < emptyArray.length; start=start+1) {
//     emptyArray.pop()
//    }
// console.log(emptyArray)

