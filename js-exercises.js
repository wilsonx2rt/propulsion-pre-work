// 1. Reverse
//Write a method that will take a string as input, and return a new string with the same letters in reverse order.

// For example: reverse('abcd') => 'dcba'

function reverse(string) {
  if(typeof string !== String){
    return 'aregument should be a string!';
  } else {
  return string.split('').reverse().join('');
  }
}
//console.log(reverse(6));

/* -------------------------------------------------------------------------- */
// 2. Factorial
// Write a method that takes an integer n in; it should return n*(n-1)*(n-2)*...*2*1. Assume n >= 0.
//
// As a special case, factorial(0) == 1.
//
// For exampe: factorial(4) => 24

function factorial(n) {
  var result = 1;
  for(var i = 1; i <= n; i++) {
    result *= i;
  }
  return result;
}
// console.log(factorial(4));
/* -------------------------------------------------------------------------- */
// 3. Longest Word
// Write a method that takes in a string. Return the longest word in the string. You may assume that the string contains only letters and spaces. You may use the String split method to aid you in your quest.
//
// For example: longest_word('This is an amazing test') => 'amazing'

function longest_word(sentence) {
  var result = "";
  var words = sentence.split(' ');
    words.forEach(word => {
      if(word.length > result.length) {
        result = word;
      }
    });
  return result;
}
// console.log(longest_word('rapidamente corren los carros por las vias de ferrocarril'));
/* -------------------------------------------------------------------------- */
// 4. Sum Nums
// Write a method that takes in an integer num and returns the sum of all integers between zero and num, up to and including num.
//
// For example: sum_nums(6) => 21

function sum_nums(num) {
  var addedNum = 0;
  for(var i = num; i > 0; i--) {
    addedNum += i;
  }
  return addedNum;
}
//console.log(sum_nums(7));
/* -------------------------------------------------------------------------- */
// 5. Time Conversion
// Write a method that will take in a number of minutes, and returns a string that formats the number into hours:minutes.
//
// For example: time_conversion(155) => '2:35'

function time_conversion(minutes) {
  var hoursStr = (minutes / 60).toFixed(2).toString().split('.');
  var hours = hoursStr[0];
  var minutes = (hoursStr[1] * .6).toFixed();
  return `${hours}:${minutes}`;
}

// console.log(time_conversion(155));
/* -------------------------------------------------------------------------- */
// 6. Count Vowels
// Write a method that takes a string and returns the number of vowels in the string. You may assume that all the letters are lower cased. You can treat "y" as a consonant.
//
// For example: count_vowels('alphabet') => 3

function count_vowels(string) {
  return string.match(/[aeiou]/g).length; // either convert to lowercase or add AEIOU to regex
}

//console.log(count_vowels('alphabet'));
/* -------------------------------------------------------------------------- */
// 7. Palindrome
// Write a method that takes a string and returns true if it is a palindrome. A palindrome is a string that is the same whether written backward or forward. Assume that there are no spaces; only lowercase letters will be given.
//
// For example:
//
// palindrome('abcd') => false
//
// palindrome('abbba') => true

function palindrome(string) {
  return string === string.split('').reverse().join('');
}

// console.log(palindrome('abbba'));
/* -------------------------------------------------------------------------- */
// 8. Most Letters
// Write a method that takes a string in and returns true if the letter "z" appears within three letters after an "a". You may assume that the string contains only lowercase letters.
//
// For example:
//
// nearby_az('abbbz') => false
//
// nearby_az('abz') => true

function nearby_az(string) {
  //return (/az/).test(string) || (/a.z/).test(string) || (/a..z/).test(string);
  // for(var i = 0; i<string.length; i++) {
  //   if(string[i] === 'a') {
  //     if(string[i+1] === 'z' || string[i+2] === 'z' || string[i+3] === 'z') {
  //       return true;
  //     } else {
  //       return false;
  //     }
  //   }
  // }
}
// console.log(nearby_az('abbbz'));
// console.log(nearby_az('a'));
// console.log(nearby_az('az'));
// console.log(nearby_az('aaz'));
// console.log(nearby_az('asaz'));
/* -------------------------------------------------------------------------- */
// 9. Two Sum
// Write a method that takes an array of numbers. If a pair of numbers in the array sums to zero, return the positions of those two numbers. If no pair of numbers sums to zero, return null.
//
// For example:
//
// two_sum([1, 3, -1, 5]) => [[0, 2]]
//
// two_sum([1, 3, -1, 5, -3]) => [[0, 2], [1, 4]]
//
// two_sum([1, 5, 3, -4]) => nil

function two_sum(nums) {
  var result = [];
  for(var i = 0; i < nums.length -1; i++) {
    for(var j = 1; j < nums.length; j++) {
      if(nums[i]+nums[j] === 0){
         result.push([nums.indexOf(nums[i]), nums.indexOf(nums[j])]);
      }
    }
  }
return result;
}
// console.log(two_sum([1, 5, 3, -4]));
// console.log(two_sum([1, 3, -1, 5]));
// console.log(two_sum([1, 3, -1, 5, -3]));
/* -------------------------------------------------------------------------- */
// 10. Is Power of Two
// Write a method that takes in a number and returns true if it is a power of 2. Otherwise, return false. You may want to use the % modulo operation. 5 % 2 returns the remainder when dividing 5 by 2; therefore, 5 % 2 == 1. In the case of 6 % 2, since 2 evenly divides 6 with no remainder, 6 % 2 == 0.
//
// For example:
//
// is_power_of_two(8) => true
//
// is_power_of_two(24) => false

function is_power_of_two(num) {
  return (Math.log(num)/Math.log(2)) % 1 === 0;
} //other solution
// console.log(is_power_of_two(8));
// console.log(is_power_of_two(24));
/* -------------------------------------------------------------------------- */
// 11. Repeat a string
// Repeat a given string (first argument) num times (second argument). Return an empty string if num is not a positive number.
//
// For example:
//
// repeat_string_num_times("abc", 3)=> abcabcabc
//
// repeat_string_num_times("abc", -1)=> ""

function repeat_string_num_times(str, num) {
  var newStr = ''
  if (num < 0) {
    return "";
  } else if (num > 0) {
    for(var i = num; i > 0; i--) {
      newStr += str;
    }
    return newStr;
  } else {
    return 'num is 0'
  }
}
// console.log(repeat_string_num_times("abc", 0));
/* -------------------------------------------------------------------------- */
// 12. Sum All Numbers in a Range
// Write a function that receives an array of two numbers as argument and returns the sum of those two numbers and all numbers between them.
//
// For example:
//
// add_all([1, 4]) => 10
//
// add_all([5, 10]) => 45

function add_all(arr) {
  var range = [];
  arr = arr.sort(function(a,b){
    return a - b;
  });
  for(var i = arr[0]; i <= arr[1]; i++) {
    range.push(i);
  }
  var sum = range.reduce((a, b){
    return a + b;
  });
  return sum;
}

// console.log(add_all([100, 1]));
/* -------------------------------------------------------------------------- */
// 13. True or False
// Write a function that checks if a value is classified as a boolean primitive. Return true or false.
//
// Boolean primitives are true and false.
//
// For example:
//
// is_it_true(true)=>true
//
// is_it_true(false)=>true
//
// is_it_true("true")=>false
//
// is_it_true(1)=>false
//
// is_it_true("false")=>false

function is_it_true(args) {
  return Boolean(args)
}

// console.log(is_it_true(true));
/* -------------------------------------------------------------------------- */
// 14. Return Largest Numbers in Arrays
// Write a function that receives an array with four nested array. The function returns an array consisting of the largest number from each provided sub-array.
//
// For exmple:
//
// largestOfFour([[13, 27, 18, 26], [4, 5, 1, 3], [32, 35, 37, 39], [1000, 1001, 857, 1]]) =>[27,5,39,1001]`
function largest_of_four(arr) {
  var result = [];
  arr.forEach(function(array){
    array.sort(function(a,b){
      return a-b;
    });
    result.push(array[array.length - 1]);
  });
  return result;
}
// console.log(largest_of_four([[13, 27, 18, 26], [4, 5, 1, 3], [32, 35, 37, 39], [1000, 1001, 857, 1]]));
/* -------------------------------------------------------------------------- */
// 15. Does it starts with Java?
// Write a JavaScript program to check if a string starts with 'Java' and false otherwise.
//
// For example:
//
// starts_with_java("JavaScript")=> true
//
// starts_with_java("Java")=> true
//
// starts_with_java("Python")=> false

function starts_with_java(str){
  var result = (/^java/gi).test(str);
  return result;
}
// console.log(starts_with_java("JavaScript"));
