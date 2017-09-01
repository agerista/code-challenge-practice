function flattenNestedArrays(arr) {
  
  // flattens arbitrarily nested arrays

  var result = [];
  var stack = arr;
  var temp;

  while (stack.length > 0) {
    temp = stack.shift();
    if (Array.isArray(temp)) {
      [].unshift.apply(stack, temp);
    }
    else {
      result.push(temp);
    }
  }
  return result;
}

flattenNestedArrays([[1,2,[3]],4]); // [1,2,3,4]
flattenNestedArrays([[1], [2, 3], [4]]); // [1,2,3,4]
flattenNestedArrays([[1,2,[3],[4],[5,6,[7]]]]); // [1,2,3,4,5,6,7]
