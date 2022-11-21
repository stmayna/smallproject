// console.log("Hello fr main.js");

let age = 25;
// console.log(age);

let sum = 0;
sum = 5;
// console.log(sum);

const isPrimaryNumber = true;
const isNewUser = false;

const res = null;
const data = null;

const persons = {
  firstname: "Mayna",
  lastname: "Siti",
  age: "23",
};

const oddNumbers = [1, 3, 4, 5];

let z = 10;
z = "Mayna";
z = true;

let f = 10;
let g = 4;

// const isEven = 10 % 2 === 0 ? "Number is even" : "Number is odd";

// console.log(2 + "3");

// console.log(Number(""));

// console.log(parseInt("5"));

// console.log(parseFloat("5.3"));

// console.log((500).toString());

// console.log(Boolean(10));

// console.log(Boolean(null));

// const num = 0;

// if (num > 0) {
//   console.log("Number is positive");
// } else if (num < 0) {
//   console.log("Number is negative");
// } else {
//   console.log("Number is zero");
// }

// const color = 10;

// switch (color) {
//   case "red":
//     console.log("Color is red");
//     break;
//   case "blue":
//     console.log("Color is blue");
//     break;
//   case "green":
//     console.log("Color is green");
//     break;
//   default:
//     console.log("Not a valid color");
// }

// for (let i = 1; i <= 5; i++) {
//   console.log("Iteration number" + i);
// }

// let i = 1;
// while (i <= 5) {
//   console.log("Iteration number" + i);
//   i++;
// }

// let j = 6;
// do {
//   console.log("Iteration number" + j);
//   i++;
// } while (j <= 5);

// const numArray = [1, 2, 3, 4, 5];

// for (const num in numArray) {
//   console.log("Iteration number" + num);
// }

function greet(username) {
  console.log("Good morning " + username);
}

// greet("Mayna");

// function add(a, b) {
//   return a + b;
// }

// const arrowSum = (a, b) => {
//   return a + b;
// };

// const arrowSumB = (a, b) => a + b;

// const amount = arrowSumB(5, 10);

// const myNum = 100;
// const myName = "Superman";

// if (true) {
//   const myName = "Mayna";
//   console.log(myName);
//   console.log(myNum);
// }

// function testFn() {
//   const myName = "Mayna";
//   console.log(myName);
//   console.log(myNum);
// }

// testFn();

// NESTED FUNCTION
let a = 10;

function outer() {
  let b = 20;
  function inner() {
    let c = 30;
    console.log(a, b, c);
  }
  inner();
}

// outer();

// CLOSURE

function outer() {
  let counter = 0;
  function inner() {
    counter++;
    console.log(counter);
  }
  return inner;
}

// const fnt = outer();
// fnt();
// fnt();

// CURRYING

function sums(a, b, c) {
  return a + b + c;
}

// console.log(sums(2, 3, 5));

function curry(fnt) {
  return function (a) {
    return function (b) {
      return function (c) {
        return fnt(a, b, c);
      };
    };
  };
}

// const curriedSum = curry(sums);
// console.log(curriedSum(2)(3)(5));

// const add2 = curriedSum(2);
// const add3 = add2(3);
// const add5 = add3(5);

// console.log(add5);

// THIS KEYWORD

function sayMyName(name) {
  console.log(`My name is ${name}`);
}

// sayMyName("Mayna");

const person = {
  name: "Mayna",
  sayMyName: function () {
    console.log(`My name is ${this.name}`);
  },
};

globalThis.name = "Superman";

function sayMyName() {
  console.log(`My name is ${this.name}`);
}

// sayMyName.call(person);
// person.sayMyName();

function Person(name) {
  this.name = name;
}

const p1 = new Person("Mayna");
const p2 = new Person("Meimei");

// console.log(p1.name, p2.name);

// sayMyName();

// PROTOTYPAL

function Person(fName, lName) {
  this.firstname = fName;
  this.lastname = lName;
}

const person1 = new Person("Mayna", "Siti");
const person2 = new Person("Siti", "Mayna");

Person.prototype.getFullName = function () {
  return this.firstname + " " + this.lastname;
};

// console.log(person1.getFullName());
// console.log(person2.getFullName());

// PROTOTYPAL INHERITANCE

function SuperHero(fName, lName) {
  Person.call(this, fName, lName);
  this.isSuperHero = true;
}

SuperHero.prototype.fightCrime = function () {
  console.log("Fighting Crime");
};

SuperHero.prototype = Object.create(Person.prototype);

const catwoman = new SuperHero("Siti", "Mayna");
SuperHero.prototype.constructor = SuperHero;
// console.log(catwoman.getFullName());

// CLASSES

class Persona {
  constructor(fName, lName) {
    this.firstname = fName;
    this.lastname = lName;
  }
  sayMyName() {
    return this.firstname + " " + this.lastname;
  }
}

const classP1 = new Persona("Siti", "Mayna");
// console.log(classP1.sayMyName());

class SuperHeroes extends Persona {
  constructor(fName, lName) {
    super(fName, lName);
    this.isSuperHero = true;
  }
  fightcrime() {
    console.log("fighting crime");
  }
}

const batman = new SuperHeroes("Mayna", "Siti");
// console.log(batman.sayMyName());

// ITERABLES AND ITERATORS

// const str = "Mayna";

// for (let i = 0; i < str.length; i++) {
//   console.log(str.charAt(i));
// }

// const arr = ["M", "a", "y", "n", "a"];

// for (let i = 0; i < arr.length; i++) {
//   console.log(arr[i]);
// }

const obj = {
  [Symbol.iterator]: function () {
    let step = 0;
    const iterator = {
      next: function () {
        step++;
        if (step === 1) {
          return { value: "Hello", done: false };
        } else if (step === 2) {
          return { value: "World", done: false };
        }
        return { value: undefined, done: true };
      },
    };
    return iterator;
  },
};

// for (const word of obj) {
//   console.log(word);
// }

// GENERATORS

function normalFunction() {
  console.log("Hello");
  console.log("World");
}

// normalFunction();

function* generatorFunction() {
  yield "Hello";
  yield "World";
}

// const generatorObject = generatorFunction();

// for (const word of generatorObject) {
//   console.log(word);
// }

// ASYNCHRONOUS JAVASCRIPT

// CALLBACKS
// Synchronous Callback: Executed immediately.

function greet(name) {
  console.log(`Hello ${name}`);
}

function higherOrderFunction(callback) {
  const name = "Mayna";
  callback(name);
}

// higherOrderFunction(greet);

let numbers = [3, 2, 4, 7, 6, 8, 3, 1, 5, 9];
numbers.sort((a, b) => a - b);
numbers.map((n) => n * 2);
numbers.filter((n) => n % 2 === 0);

// Asynchronous Callbacks: often use to continue codde execution after asynchronous operation has completed.
// Callback: used to delay execution of a function until a particular time or event has occured.

function greets(name) {
  console.log(`Hello ${name}`);
}

// setTimeout(greet, 2000, "Mayna");

// function callback() {
//   document.getElementById("demo").innerHTML = "Hello World";
// }

// document.getElementById("btn").addEventListener("click", callback);

// CALLBACK JQUERY

// $.get("url", function (data) {
//   $(".result").html(data);
//   alert("Load was performed");
// });

const promise = new Promise((resolve, reject) => {
  setTimeout(() => {
    resolve("Bringin tacos.");
  }, 3000);

  setTimeout(() => {
    reject("Not bringing tacos, food truck not there.");
  }, 3000);
});

const onFulfillment = (result) => {
  console.log(result);
  console.log("Set up the table to eat tacos.");
};

const onRejection = (error) => {
  console.log(error);
  console.log("Start cooking pasta.");
};

// promise.then(onFulfillment, onRejection);
// promise.catch(onRejection);
// promise.then(onFulfillment).catch(onRejection);

const promise1 = Promise.resolve(3);
const promise2 = 42;
const promise3 = new Promise((resolve, reject) => {
  setTimeout(resolve, 100, "foo");
});

// Promise.all([promise1, promise2, promise3]).then((values) => {
//   console.log(values);
// });

// Promise.allSettled([promise1, promise2, promise3]).then((values) => {
//   console.log(values);
// });

// Promise.race([promise1, promise2, promise3]).then((values) => {
//   console.log(values);
// });

// ASYNC AWAIT
async function hello() {
  let promise = new Promise((resolve, reject) => {
    setTimeout(() => resolve("Hello"), 1000);
  });

  let result = await promise;

  console.log(result);
}

// hello();

function resolveHello() {
  return new Promise((resolve) => {
    setTimeout(function () {
      resolve("Hello");
    }, 2000);
  });
}

function resolveWorld() {
  return new Promise((resolve) => {
    setTimeout(function () {
      resolve("World");
    }, 1000);
  });
}

async function sequentialStart() {
  const hello = await resolveHello();
  console.log(hello);

  const world = await resolveWorld();
  console.log(world);
}

// sequentialStart();

async function concurrentStart() {
  const hello = resolveHello();
  const world = resolveWorld();

  console.log(await hello);
  console.log(await world);
}

// concurrentStart();

function parallel() {
  Promise.all([
    (async () => console.log(await resolveHello()))(),
    (async () => console.log(await resolveWorld()))(),
  ]);
}

// parallel();

async function parallelB() {
  await Promise.all([
    (async () => console.log(await resolveHello()))(),
    (async () => console.log(await resolveWorld()))(),
  ]);

  console.log("Finally");
}

// parallelB();

// EVENT LOOP
