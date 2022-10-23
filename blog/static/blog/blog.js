function sayHello(yourName) {
  if (yourName === undefined) {
      console.log('Hello, no name')
  } else {
       console.log('Hello, ' + yourName)
  }
}

const yourName = 'Your Name'  // Put your name here

console.log('Before setTimeout')

setTimeout(() => {
    sayHello(yourName)
  }, 2000
)

console.log('After setTimeout')