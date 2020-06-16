function check(){
  userid_value = document.getElementById('name').value;
  password_value = document.getElementById('pass').value;
  zipcode_value = document.getElementById('zip').value;
  //sentence_value = document.getElementById('sntnc').value;

  regObj = new RegExp(/<("[^"]*"|'[^']*'|[^'">])*>/, "g");
  result1 = userid_value.match(regObj);
  result2 = password_value.match(regObj);
  result3 = zipcode_value.match(regObj);
  //result4 = sentence_value.match(regObj);


  if(userid_value.length <= 0 || password_value.length <= 0 || zipcode_value.length <= 0){
    ret = false; alert("userid, password & zipcode are necessary.");
  }else if(result1){
    ret = false; alert("HTMLタグは使えません");
  }else if(result2){
    ret = false; alert("HTMLタグは使えません");
  }else if(result3){
    ret = false; alert("HTMLタグは使えません");
  }else{
    ret = true;
  }
  return ret;
}

function check2(){
  userid_value = document.getElementById('name').value;
  password_value = document.getElementById('pass').value;
  regObj = new RegExp(/<("[^"]*"|'[^']*'|[^'">])*>/, "g");
  result1 = userid_value.match(regObj);
  result2 = password_value.match(regObj);

  if(userid_value.length <= 0 || password_value.length <= 0){
    ret = false; alert("userid & password are necessary.");
  }else if(result1){
    ret = false; alert("HTMLタグは使えません");
  }else if(result2){
    ret = false; alert("HTMLタグは使えません");
  }else{
    ret = true;
  }
  return ret;
}
