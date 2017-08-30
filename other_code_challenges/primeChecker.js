function primeChecker(num) {
    
  // Checks if a number is prime (only divisible by 1 and itself)
  // assumes number is greater than 0

  if (num < 2) {
    return false;
  }

  if (num === 2) {
    return true;
  }

  if (num % 2 === 0) {
    return false;
  }

  var n = 3;

  while (n * n <= num) {

    if (num % n === 0) {
      return false;
    }

    else {
      num += 2;
    }
  }

  return true;
}

primeChecker(3); // return True
primeChecker(4); // return False
primeChecker(23); // return True
primeChecker(25); // return False