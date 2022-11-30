
let id = document.getElementById('id');
let password = document.getElementById('password');
let sign = document.getElementById('sign');
sign.addEventListener('click', getData);
let httpResquest;

function getData() {
    alert("눌렸습니다");
    console.log(id);
    let inputId = id.value;
    let inputPassword = password.value;
    let reqJson = new Object();
    reqJson.id = inputId;
    reqJson.password = inputPassword;
    httpResquest = new XMLHttpRequest();
    httpResquest.onreadystatechange = () =>{
        if(httpResquest.readyState === XMLHttpRequest.DONE){
            if(httpResquest.status === 200){
                alert(httpResquest.responseText);
            }else{
                alert("error");
            }
        }
    }
    httpResquest.open("POST", "http://localhost:8000/survey", true);
    httpResquest.responseType = "json";
    httpResquest.setRequestHeader("Content-Type", "application/json");
    httpResquest.send(JSON.stringify(reqJson));


}
//https://kyounghwan01.github.io/blog/JS/JSbasic/getElementById/#%E1%84%89%E1%85%A1%E1%84%8B%E1%85%AD%E1%86%BC%E1%84%87%E1%85%A5%E1%86%B8

const mode = document.getElementById("jsmode");
mode.addEventListener("click", function() {
  if (mode.innerText === "바뀌기 전 text") {
    mode.innerText = "바뀐 text!";
  } else {
    mode.innerText = "바뀌기 전 text";
  }
});