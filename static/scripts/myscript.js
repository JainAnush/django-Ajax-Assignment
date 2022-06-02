let ajaxreq = null;
function process() {
  console.log("in process function");
  ajaxreq = new XMLHttpRequest();
  ajaxreq.onreadystatechange = processresult;
  ajaxreq.open("GET", "/api", true);
  ajaxreq.send(null);
}
function processresult() {
  if (ajaxreq.readyState == 4) {
    var response = JSON.parse(ajaxreq.responseText);
    console.log(typeof response);
    console.log(response);
    correctanslist = [];

    for (obj of response) {
      correctanslist.push(obj["fields"]["correctans"]);
    }
    console.log("size :" + correctanslist.length);
    useranslist = [];
    for (let i = 0; i < correctanslist.length; i++) {
      if (document.getElementById(String(i) + "q1").checked) {
        useranslist.push(1);
      } else if (document.getElementById(String(i) + "q2").checked) {
        useranslist.push(2);
      } else if (document.getElementById(String(i) + "q3").checked) {
        useranslist.push(3);
      } else {
        useranslist.push(4);
      }
    }
    let ajaxreq2 = new XMLHttpRequest();
    ajaxreq2.onreadystatechange = function () {
      if (ajaxreq2.readyState == 4) {
        let obj = JSON.parse(ajaxreq2.responseText);
        console.log(
          obj.score + "," + obj.right + "," + obj.wrong + "," + obj.percentage
        );
        let div = document.getElementById("title");
        div.innerHTML = "<h1>RESULT PAGE<h1>";
        div2 = document.getElementById("result");
        result = "<center><h1>SCORE : " + obj.score + "<h1>";
        result += "<h1>CORRECT :" + obj.right + "<h1>";
        result += "<h1>WRONG :" + obj.wrong + "<h1>";
        result += "<h1>PERCENTAGE :" + obj.percentage.toFixed(2) + "<h1>";
        if (obj.percentage >= 50) {
          result += "<h1>CONGRATS YOU PASSED THE TEST<h1></center>";
        } else {
          result += "<h1>SORRY YOU FAILED THE TEST<h1></center>";
        }
        div2.innerHTML = result;
      }
    };
    ajaxreq2.open(
      "GET",
      "/result?userans=" +
        JSON.stringify(useranslist) +
        "&corrans=" +
        JSON.stringify(correctanslist),
      true
    );
    ajaxreq2.send(null);
    // console.log("size 2 :" + useranslist.length);
    // for (let j = 0; j < correctanslist.length; j++) {
    //   if (correctanslist[j] == useranslist[j]) {
    //     score += 4;
    //     correct++;
    //   } else {
    //     score -= 1;
    //     wrong += 1;
    //   }
    // }
    // console.log("SCORE :" + score);
    // let div = document.getElementById("result");
    // let result = "<center><h1> SCORE :" + score + "<h1>";
    // result += "<h1>Correct : " + correct + "<h1>";
    // result += "<h1>Wrong : " + wrong + "<h1>";
    // result +=
    //   "<h1>Percentage : " +
    //   ((score / (correctanslist.length * 4)) * 100).toFixed(2) +
    //   "<h1>";
    // if ((score / (correctanslist.length * 4)) * 100 > 50) {
    //   result += "<h1>CONGRATS YOU PASSED THE TEST<h1>";
    // } else {
    //   result += "<h1>SORRY YOU COULD NOT PASS THE TEST THIS TIME<h1></center>";
    // }
    // div.innerHTML = result;
    // div2 = document.getElementById("title");
    // div2.innerHTML = "<h1> RESULT PAGE<h1>";
  }
}
