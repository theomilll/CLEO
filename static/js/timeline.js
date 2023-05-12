var listItems = document.querySelectorAll("#progressbar li");


var currentProgress = 0;

function advanceProgress() {
  if(currentProgress < listItems.length){
    listItems[currentProgress].classList.add("active");
    currentProgress++;
  } else {
    clearInterval(progressInterval);
  }
}

var progressInterval = setInterval(advanceProgress, 2500);