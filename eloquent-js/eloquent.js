// Eloquent JS Problems

// “Looping a triangle
//
// Write a loop that makes seven calls to console.log to output the following triangle:
//
// #
// ##
// ###
// ####
// #####
// ######
// #######
// It may be useful to know that you can find the length of a string by writing .length after it.
//
// var abc = "abc";
// console.log(abc.length);
//  → 3”

// Solution
// var str = '';
// for (var i = 0; i < 7; i++) {
//   str += '#';
//   console.log(str);
// }

// FizzBuzz
//
// Write a program that uses console.log to print all the numbers from 1 to 100, with two exceptions. For numbers divisible by 3, print "Fizz" instead of the number, and for numbers divisible by 5 (and not 3), print "Buzz" instead.
//
// When you have that working, modify your program to print "FizzBuzz", for numbers that are divisible by both 3 and 5 (and still print "Fizz" or "Buzz" for numbers divisible by only one of those).
//
// (This is actually an interview question that has been claimed to weed out a significant percentage of programmer candidates. So if you solved it, you’re now allowed to feel good about yourself.)”

// Solution
// for (var i = 1; i <= 100; i++) {
//   if (i % 3 === 0) {
//     console.log('fizz');
//   } else if (i % 5 === 0) {
//     console.log('buzz');
//   } else {
//       console.log(i);
//   }
// }


// Chapter 3
// Exercises
//
// Minimum
//
// The previous chapter introduced the standard function Math.min that returns its smallest argument. We can do that ourselves now. Write a function min that takes two arguments and returns their minimum.

// Solution
// function min(a, b) {
//   if (a < b) {
//     return a;
//   } else {
//     return b;
//   }
// }
//
// console.log(min(100, 200));

//
// Recursion
//
// We’ve seen that % (the remainder operator) can be used to test whether a number is even or odd by using % 2 to check whether it’s divisible by two. Here’s another way to define whether a positive whole number is even or odd:
//
// Zero is even.
//
// One is odd.
//
// For any other number N, its evenness is the same as N - 2.
//
// Define a recursive function isEven corresponding to this description. The function should accept a number parameter and return a Boolean.
//
// Test it on 50 and 75. See how it behaves on -1. Why? Can you think of a way to fix this?”
//

// Review recursion


// “Bean counting
//
// You can get the Nth character, or letter, from a string by writing "string".charAt(N), similar to how you get its length with "s".length. The returned value will be a string containing only one character (for example, "b"). The first character has position zero, which causes the last one to be found at position string.length - 1. In other words, a two-character string has length 2, and its characters have positions 0 and 1.
//
// Write a function countBs that takes a string as its only argument and returns a number that indicates how many uppercase “B” characters are in the string.”
//
// “Next, write a function called countChar that behaves like countBs, except it takes a second argument that indicates the character that is to be counted (rather than counting only uppercase “B” characters). Rewrite countBs to make use of this new function.”

//Solution

// function countBs(string) {
//   var count = 0;
//   for (var i = 0; i < string.length; i++) {
//     if (string[i] === "B") {
//       count += 1;
//     }
//   }
//   return count;
// }
//
// console.log(countBs('BaBaganoushB'));
//
// function countChar(string, char) {
//   var count = 0;
//   for (var i = 0; i < string.length; i++) {
//     if (string[i] === char) {
//       count += 1;
//     }
//   }
//   return count;
// }
//
// console.log(countChar('BaBaganoushB', 'B'));
