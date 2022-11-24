const answerForm = document.forms["answerform"];
const answer = document.getElementById("answerBox");
const ans_input = document.getElementById("myform").elements["Name"];

answerForm.addEventListener("submit", async (e) => {
  e.preventDefault();

  var password = '';
  var status = '';
  var myHeaders = new Headers();
  myHeaders.append("answer", `${ans_input.value}`);
  var requestOptions = {
    method: "GET",
    headers: myHeaders,
    redirect: "follow",
  };

  await fetch("http://localhost:5000/TopGTate", requestOptions)
    .then((response) => response.json())
    .then((result) => {status = result.status;password = result.pass;})
    .catch((error) => console.log("error", error));

    if( status == 'success') {
        answer.style.display = "flex";
        document.getElementById("password").innerHTML = password;
    }
    else {
        alert("Try again");
    }

  ans_input.value = "";
});
