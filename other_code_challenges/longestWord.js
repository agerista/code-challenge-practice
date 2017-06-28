function findLongestWord(str) {
  
  var count = 0;
  var phrase = str.split(" ");
  
  for (var i=0; i<phrase.length; i++) {
    
    if (phrase[i].length > count) {
      count = phrase[i].length;
    }
  }
  
  return count;
}

findLongestWord("The quick brown fox jumped over the lazy dog");
findLongestWord("May the force be with you");
findLongestWord("Google do a barrel roll");
findLongestWord("What is the average airspeed velocity of an unladen swallow");