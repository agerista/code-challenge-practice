function palindrome(str) {
  
  var check = str.toLowerCase().replace(/[_:(-/,.\s]+/g, "");
  var reverse = check.split("").reverse().join("");
  return (check === reverse);
}

palindrome("eye");
palindrome("race car");
palindrome("not a palindrome");