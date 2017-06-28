function titleCase(str) {
  
  var phrase = str.toLowerCase().split(' ');
  console.log(phrase);
  var title = [];
  
  for (var i=0; i<phrase.length; i++){
    
    title.push(phrase[i][0].toUpperCase() + phrase[i].slice(1));
  }
  return title.join(" ");
}
titleCase("I'm a little tea pot");
titleCase("sHoRt AnD sToUt");
titleCase("HERE IS MY HANDLE HERE IS MY SPOUT");